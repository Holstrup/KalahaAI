from Game import Kalaha
import random
import time

def play(human = False, delay = 0):
    game = Kalaha()
    player = game.player1


    while not game.terminal_test(game.get_state()):
        time.sleep(delay)

        if player == game.player1 and human:
            hole=-1

            #Let player choose until valid move
            while hole not in game.possible_actions(player,game.get_state()):
                print(game.possible_actions(player))
                hole = int(input("Please choose hole: "))


            print("Player Chooses Hole {}".format(hole))

            new_state,same_player = game.take(player, hole,game.get_state())
            game.set_state(new_state)
            if not same_player:
                player = game.player2
            else:
                print("Player Goes Again")

        elif player == game.player1:
            hole = random.choice(game.possible_actions(player,game.get_state())) # <- AI agents action goes here
            print("Agent 1 Chooses Hole {}".format(hole))
            new_state,same_player = game.take(player, hole,game.get_state())
            game.set_state(new_state)
            if not same_player:
                player = game.player2
            else:
                print("Agent Goes Again")

        else:
            print(game.minimax(game.get_state(),player,game.player1,2))
            input("")
            hole = random.choice(game.possible_actions(player,game.get_state()))  # <- AI agents action goes here
            print("Agent 2 Chooses Hole {}".format(hole))
            new_state,same_player = game.take(player, hole,game.get_state())
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
    play(delay=1)