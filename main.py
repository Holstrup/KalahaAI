from Game import Kalaha
import time
import copy
from Agent import Agent
import random

def main(human = False, delay = 0):
    game = Kalaha(starting_player=0)
    ai_1 = Agent()
    ai_2 = Agent()

    while not game.terminal_test():
        time.sleep(delay)
        player = game.state[3]

        if player == game.player1 and human:
            print("Human Turn: ")
            hole = int(input())
            print("Player Chooses Hole {}".format(hole))
            game.take(hole)

        elif player == game.player1:
            game_copy = copy.deepcopy(game)
            hole = ai_1.find_next_move(game_copy)
            # hole = random.choice(game.possible_actions())
            print("Agent 1 Chooses Hole {}".format(hole))
            game.take(hole)

        else:
            game_copy = copy.deepcopy(game)
            hole = ai_2.find_next_move(game_copy) # <- AI agents action goes here
            # hole = random.choice(game.possible_actions())
            print("Agent 2 Chooses Hole {}".format(hole))
            game.take(hole)

        game.print_board()
    game.finalize_game()
    game.print_board()




if __name__ == "__main__":
    main(delay=0.0, human=False)