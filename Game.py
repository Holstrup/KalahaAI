import random
import time
from copy import copy, deepcopy


class Kalaha:

    def __init__(self):
        """
        Parameters
        """
        self.board_size = 6
        self.stones = 4

        """
        State and variables
        """
        self.state = [[self.stones] * self.board_size, [self.stones] * self.board_size, [0, 0]]

        self.player1 = 0
        self.player2 = 1

    def terminal_test(self, state):
        return sum(state[0]) == 0 or sum(state[1]) == 0

    def finalize_game(self, state=None, game_over=False):
        # if game_over==True then state=self.state
        if game_over:
            state = self.state
        if sum(state[0]) == 0:
            print(sum(state[1]))
            state[2][1] += sum(state[1])
            state[1] = [0] * self.board_size
        elif sum(state[1]) == 0:
            state[2][0] += sum(state[0])
            state[0] = [0] * self.board_size
        return state

    def print_board(self,state):
        print("\n")
        print(" " * 2 + "-" * 13)
        print(" | " + "|".join(str(hole) for hole in reversed(state[self.player2])) + " | ")

        print(str(state[2][self.player2]) + "|" + " " * 13 + "|" + str(state[2][self.player1]))

        print(" | " + "|".join(str(hole) for hole in state[self.player1]) + " | ")
        print(" " * 2 + "-" * 13)
        print("\n")
        #print("-" * 10)

    def possible_actions(self, player,state):
        possible_holes = []
        for i, hole in enumerate(state[player]):
            if hole > 0:
                possible_holes.append(i)
        return possible_holes

    def take(self, player, hole, state):
        new_state = deepcopy(state)

        stones = new_state[player][hole]
        new_state[player][hole] = 0

        row = player

        while stones > 0:
            hole += 1

            # If we need to go from one row to the other (at the end of a row)
            if hole == self.board_size and self.stones > 0:
                new_state[2][row] += 1
                stones -= 1
                if row == 1:
                    row = 0
                else:
                    row = 1
                hole = 0

                if stones > 0:
                    stones -= 1
                    new_state[row][hole] += 1

                # If we put the last stone in our mancala -> Same player goes again
                else:
                    return new_state, True

            else:

                # If 1 stone left and next hole is empty and youre on your own side of the board
                if stones == 1 and new_state[row][hole] == 0 and row == player:
                    new_state[row][hole] += 1
                    stones -= 1

                    # Get all stones from opposite hole
                    if row == player:
                        if player == 0:
                            new_state[2][player] += new_state[1][5 - hole]
                            new_state[1][5 - hole] = 0
                        else:
                            new_state[2][player] += new_state[0][5 - hole]
                            new_state[0][5 - hole] = 0
                elif stones > 0:
                    new_state[row][hole] += 1
                    stones -= 1

        return new_state, False

    def set_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state

    def evaluate(self, state, player, opponent):
        print("player {0}. opponent: {1}. state: {2}. Score: {3}".format(player,opponent,state,state[2][player] - state[2][opponent]))
        print("____________")
        return state[2][player] - state[2][opponent]

    def get_children(self, player,state):

        children_spaces = []

        for move in self.possible_actions(player,state):
            children_spaces.append(self.take(player, move,state))

        return children_spaces

    def minimax(self, state, player, opponent, depth):
        print("Player {0}'s turn".format(player))

        print("depth: {0}".format(depth))
        if self.terminal_test(state):
            self.finalize_game(state=state)
            print("TERMINAL")
            return self.evaluate(state,player, opponent)
        elif depth == 0:

            return self.evaluate(state,player, opponent)

        elif player == self.player2: #If ai agent go for max difference

            best_val = -1000

            moves = self.possible_actions(player,state)

            for move in moves:

                new_state,go_again=self.take(player,move,state)
                self.print_board(new_state)

                val = self.minimax(new_state, opponent, player, depth - 1)


                best_val = max(best_val, val)

            print("BEST VALUE: {0}  FOR VALUE {1} for player{2}".format(best_val,depth,player))

            return best_val

        elif player == self.player1:


            best_val = 1000
            moves = self.possible_actions(player, state)

            for move in moves:
                new_state, go_again = self.take(player, move, state)
                print(move)
                self.print_board(new_state)

                val = self.minimax(new_state, opponent, player, depth - 1)

                best_val = min(best_val, val)
            print("BEST VALUE: {0}  FOR VALUE {1} for player{2}".format(best_val, depth, player))

            return best_val


