from Game import Kalaha
import random
import time

def main(human = False, delay = 0):
    game = Kalaha()
    player = game.player1

    while not game.terminal_test():
        time.sleep(delay)

        if player == game.player1 and human:
            hole = int(input())
            print("Player Chooses Hole {}".format(hole))

            same_player = game.take(player, hole)
            if not same_player:
                player = game.player2
            else:
                print("Player Goes Again")

        elif player == game.player1:
            hole = random.choice(game.possible_actions(player)) # <- AI agents action goes here
            print("Agent 1 Chooses Hole {}".format(hole))
            same_player = game.take(player, hole)
            if not same_player:
                player = game.player2
            else:
                print("Agent Goes Again")

        else:
            hole = random.choice(game.possible_actions(player))  # <- AI agents action goes here
            print("Agent 2 Chooses Hole {}".format(hole))
            same_player = game.take(player, hole)
            if not same_player:
                player = game.player1
            else:
                print("Agent Goes Again")

        game.print_board()
    game.finalize_game()
    game.print_board()




if __name__ == "__main__":
    main(delay=1)