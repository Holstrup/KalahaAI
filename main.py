from copy import deepcopy

from AI_Agent import AI
from Game import Kalaha
import random
import time

def play(human = False, delay = 0):
    game = Kalaha()
    player = game.player2
    agent1 = AI(4,True,False,False)
    agent2 = AI(4,True,False,False)

    while not game.terminal_test(game.get_state()):
        time.sleep(delay)

        if player == game.player1 and human:
            hole = -1
            #Let player choose until valid move
            while hole not in game.possible_actions(player,game.get_state()):
                print(game.possible_actions(player,game.get_state()))
                hole = int(input("Please choose hole: "))
            print("Player Chooses Hole {}".format(hole))

            new_state,same_player = game.take(player, hole,game.get_state())
            game.set_state(new_state)
            if not same_player:

                player = game.player2
            else:
                print("Player Goes Again")

        elif player == game.player1:
            #input of AI is depth of minimax

            game_copy = deepcopy(game)
            best_move = agent1.get_best_move(game_copy, game.get_state(), maximizing_player=False,pruning=True)

            print("Agent 1 Chooses Hole {}".format(best_move))
            new_state, same_player = game.take(player, best_move, game.get_state())
            game.set_state(new_state)
            if not same_player:
                player = game.player2

            else:
                print("Agent Goes Again")

        else:
            # input of AI is depth of minimax

            game_copy=deepcopy(game)
            best_move=agent2.get_best_move(game_copy,game.get_state(),maximizing_player=True,pruning=True)


            print("Agent 2 Chooses Hole {}".format(best_move))
            new_state,same_player = game.take(player, best_move,game.get_state())
            game.set_state(new_state)
            if not same_player:

                player = game.player1
            else:
                print("Agent Goes Again")



        game.print_board(game.get_state())

    #When one player runs out of stones
    game.finalize_game(game_over=True)
    game.print_board(game.get_state())




if __name__ == "__main__":
    play(delay=0)
