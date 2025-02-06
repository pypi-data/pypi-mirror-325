#pragma once
#include <torch/extension.h>
#include "chess_consts.h"
#include "moves/kingside_castling.cu"
#include "moves/queenside_castling.cu"
#include "moves/promotion.cu"
#include "moves/pawn.cu"
#include "moves/doublepush.cu"
#include "moves/enpassant.cu"
#include "moves/knight.cu"
#include "moves/king.cu"
#include "moves/rook.cu"
#include "moves/bishop.cu"
#include "moves/queen.cu"
#include "chess_attacks.cu"

__global__ void step_kernel(
    torch::PackedTensorAccessor32<int  , 2 , torch::RestrictPtrTraits> boards  ,
    torch::PackedTensorAccessor32<int  , 1 , torch::RestrictPtrTraits> players ,
    torch::PackedTensorAccessor32<int  , 2 , torch::RestrictPtrTraits> actions ,
    torch::PackedTensorAccessor32<float, 2 , torch::RestrictPtrTraits> rewards ,
    torch::PackedTensorAccessor32<bool , 1 , torch::RestrictPtrTraits> dones
) {
    // performs a standard action
    // returns 0 if everything is ok
    // returns 1 if the action was a standard action but the conditions were not met

    const size_t env = blockIdx.x * blockDim.x + threadIdx.x;
    if (env < boards.size(1)) {

        const unsigned char source = actions[0][env] * 8 + actions[1][env];
        const unsigned char target = actions[2][env] * 8 + actions[3][env];
        const unsigned char prev_action = WHITE_PREV1 + 10*players[env];
        const unsigned char enemy_pawn = ((players[env] + 1) % 2) * 6 + WHITE_PAWN;
        const unsigned char enemy_queen = ((players[env] + 1) % 2) * 6 + WHITE_QUEEN;

        const bool pawn_not_moved = (
            pawn_move       (env, players, boards, actions) &
            doublepush_move (env, players, boards, actions) &
            enpassant_move  (env, players, boards, actions) &
            promotion_move  (env, players, boards, actions)
        );

        const bool not_capturing = (
            (boards[target][env] < enemy_pawn) & 
            (boards[target][env] > enemy_queen)
        );

        const bool is_repetition = (
            (boards[prev_action+5][env] == actions[0][env]) &
            (boards[prev_action+6][env] == actions[1][env]) &
            (boards[prev_action+7][env] == actions[2][env]) &
            (boards[prev_action+8][env] == actions[3][env]) &
            (boards[prev_action+9][env] == actions[4][env])
        );


        // make action
        const bool is_action_ok = 
            (((actions[4][env] != 0) | (source != target)) &
            !(
                kingside_castle_move  ( env, players, boards, actions) &
                queenside_castle_move ( env, players, boards, actions) &
                knight_move           ( env, players, boards, actions) &
                king_move             ( env, players, boards, actions) &
                rook_move             ( env, players, boards, actions) &
                bishop_move           ( env, players, boards, actions) &
                queen_move            ( env, players, boards, actions) &
                pawn_not_moved 
            )
        );
        
        // current player king not attacked
        const unsigned char king_row = boards[KING_POSITION + players[env] * 2 + 0][env];
        const unsigned char king_col = boards[KING_POSITION + players[env] * 2 + 1][env];
        const bool is_king_ok = count_attacks(env, king_row, king_col, players, boards) == 0;
        const unsigned char player = players[env];
        const unsigned char enemy  = (players[env] + 1) % 2;
        const bool is_50 = boards[RULE50][env] >= 100;
        const bool is_3fold = boards[THREEFOLD][env] >= 6;

        // zero reward if action ok
        // the action was not allowed or uncovered the king
        rewards[player][env] = (
            (( is_action_ok &  is_king_ok) & !(is_50 | is_3fold)) * +0.0f +
            ((!is_action_ok | !is_king_ok) & !(is_50 | is_3fold)) * -1.0f + 
            (is_50 | is_3fold) * 0.5f
        ) * !dones[env]; // reward is zero if the game was over

        // if the player's action left the king uncovered, enemy get +1
        // otherwise nothing
        rewards[enemy][env] = (
            (!is_king_ok & !(is_50 | is_3fold)) * +1.0f + 
            ( is_king_ok & !(is_50 | is_3fold)) * +0.0f + 
            (is_50 | is_3fold) * 0.5f
        ) * !dones[env]; // reward is zero if the game was over

        // if one makes an illegal action, or 
        // if one leave the king in check, or
        // if the game is a draw, or
        // if the game was already terminated
        dones[env] = !is_action_ok | !is_king_ok | is_50 | is_3fold | dones[env];

        // set prev action to current action
        boards[prev_action+5][env] = boards[prev_action+0][env];
        boards[prev_action+6][env] = boards[prev_action+1][env];
        boards[prev_action+7][env] = boards[prev_action+2][env];
        boards[prev_action+8][env] = boards[prev_action+3][env];
        boards[prev_action+9][env] = boards[prev_action+4][env];
        boards[prev_action+0][env] = actions[0][env];
        boards[prev_action+1][env] = actions[1][env];
        boards[prev_action+2][env] = actions[2][env];
        boards[prev_action+3][env] = actions[3][env];
        boards[prev_action+4][env] = actions[4][env];
        boards[RULE50][env]        = (boards[RULE50][env] + 1) * pawn_not_moved * not_capturing;
        boards[THREEFOLD][env]     = (boards[THREEFOLD][env] + 1) * is_repetition;

        // switch player
        players[env] = 1 - players[env];
    }
}



    

