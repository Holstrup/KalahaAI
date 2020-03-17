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

        self.best_move = {}

    def terminal_test(self, state):
        return sum(state[0]) == 0 or sum(state[1]) == 0

    def finalize_game(self, state=None, game_over=False):
        # if game_over==True then state=self.state
        if game_over:
            state = self.state
        if sum(state[0]) == 0:
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

    def evaluate(self, state):
            return state[2][self.player2] - state[2][self.player1]

    def get_children(self, player,state):

        children_spaces = []

        for move in self.possible_actions(player,state):
            children_spaces.append(self.take(player, move,state))

        return children_spaces

    def get_best_move(self,key):
        if key == 0:
            return 0
        else:
            return self.best_move[key]

    def minimax(self, state, maximizing_player, depth,alpha,beta,pruning):

        if self.terminal_test(state):

            self.finalize_game(state=state)
            return self.evaluate(state)

        elif depth == 0:

            return self.evaluate(state)

        elif maximizing_player:

            best_val = float("-inf")

            moves = self.possible_actions(self.player2,state)

            for move in moves:

                new_state,go_again = self.take(self.player2,move,state)

                val = self.minimax(new_state, go_again, depth - 1,alpha,beta,pruning)

                if val>best_val:
                    self.best_move[depth] = move
                best_val = max(best_val, val)
                #self.print_board(new_state)
                alpha = max(alpha, best_val)

                if beta <= alpha and pruning:

                    break
            return best_val

        elif not maximizing_player:

            best_val = float("inf")

            moves = self.possible_actions(self.player1, state)

            for move in moves:

                new_state, go_again = self.take(self.player1, move, state)

                val = self.minimax(new_state, not go_again, depth - 1,alpha,beta,pruning)

                best_val = min(best_val, val)
                #self.print_board(new_state)

                beta = min(beta, best_val)

                if beta <= alpha and pruning:

                    break


            return best_val


