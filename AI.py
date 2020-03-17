from KalahaAI.Game import Kalaha
import math


def eval(state):
    return state[2][0] - state[2][1]

def minimax(game, depth, max_or_min, alpha, beta, path=[]):

    #print(max_or_min, depth)

    if depth == 0:
        return eval(game.state)

    if max_or_min == 'max':
        max_eval = -math.inf
        for hole in game.possible_actions(player=0)[:2]:
            new_game = game
            new_game.take(player=0, hole=hole)
            current_eval = minimax(new_game, depth-1, 'min', alpha, beta)
            max_eval = max(max_eval, current_eval)
            alpha = max(alpha, current_eval)
            if beta <= alpha:
                break
        return max_eval

    elif max_or_min == 'min':
        min_eval = math.inf
        for hole in game.possible_actions(player=1)[:2]:
            new_game = game
            new_game.take(player=1, hole=hole)
            current_eval = minimax(new_game, depth-1, 'max', alpha, beta)
            min_eval = min(min_eval, current_eval)
            beta = min(beta, current_eval)
            if beta <= alpha:
                break
        return min_eval



TheGame = Kalaha()

yo = minimax(TheGame, 3, 'max', -math.inf, math.inf, [])
#print("FINAL VALUE:", yo)