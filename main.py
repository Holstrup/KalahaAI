from Game import Kalaha
import time
import copy
from Agent import Agent
import random
from MCTS.State import State
from MCTS.MCTS import MCTS

def main(human = False):
    game = Kalaha(starting_player=0)
    ai_1 = Agent()
    ai_2 = Agent()

    while not game.terminal_test():
        player = game.state[3]

        if player == game.player1 and human:
            print("Human Turn: ")
            hole = int(input())
            print("Player Chooses Hole {}".format(hole))
            game.take(hole)

        elif player == game.player1:
            game_copy = copy.deepcopy(game)
            hole = monte_carlo_pred(game_copy.state, 3000) # <- MCTS
            # hole = ai_1.find_next_move(game_copy)
            print("Agent 1 Chooses Hole {}".format(hole))
            game.take(hole)

        else:
            game_copy = copy.deepcopy(game)
            # hole = monte_carlo_pred(game_copy.state, 100) # <- MCTS
            hole = ai_2.find_next_move(game_copy) # <- AI agents action goes here
            print("Agent 2 Chooses Hole {}".format(hole))
            game.take(hole)

        game.print_board()
    game.finalize_game()
    game.print_board()


def monte_carlo_pred(curr_state, iterations):
    s0 = State(curr_state)
    mcts = MCTS(s0)
    for i in range(iterations):
        n0 = mcts.root_node
        mcts.MCTS(n0)
    return mcts.robust_child()




if __name__ == "__main__":
    main(human=False)