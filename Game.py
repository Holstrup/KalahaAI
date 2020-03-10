import random
import time

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
        self.state = [[self.stones]*self.board_size, [self.stones]*self.board_size, [0,0]]

        self.player1 = 0
        self.player2 = 1



    def terminal_test(self):
        return sum(self.state[0]) == 0 or sum(self.state[1]) == 0


    def finalize_game(self):
        if sum(self.state[0]) == 0:
            print(sum(self.state[1]))
            self.state[2][1] += sum(self.state[1])
            self.state[1] = [0] * self.board_size
        elif sum(self.state[1]) == 0:
            self.state[2][0] += sum(self.state[0])
            self.state[0] = [0] * self.board_size



    def print_board(self):
        print("\n")
        print(" "*2 + "-"*13)
        print(" | " + "|".join(str(hole) for hole in reversed(self.state[self.player2])) + " | ")

        print(str(self.state[2][self.player2]) + "|" + " " * 13 + "|" + str(self.state[2][self.player1]))

        print(" | " + "|".join(str(hole) for hole in self.state[self.player1]) + " | ")
        print(" " * 2 + "-" * 13)
        print("\n")
        print("-"*10)


    def possible_actions(self, player):
        possible_holes = []
        for i, hole in enumerate(self.state[player]):
            if hole > 0:
                possible_holes.append(i)
        return possible_holes


    def take(self, player, hole):
        stones = self.state[player][hole]
        self.state[player][hole] = 0

        row = player

        while stones > 0:
            hole += 1

            # If we need to go from one row to the other (at the end of a row)
            if hole == self.board_size and self.stones > 0:
                self.state[2][row] += 1
                stones -= 1
                if row == 1:
                    row = 0
                else:
                    row = 1
                hole = 0

                if stones > 0:
                    stones -= 1
                    self.state[row][hole] += 1

                # If we put the last stone in our mancala -> Same player goes again
                else:
                    return True

            else:

                # If 1 stone left and next hole is empty and youre on your own side of the board
                if stones == 1 and self.state[row][hole] == 0 and row == player:
                    self.state[row][hole] += 1
                    stones -= 1

                    # Get all stones from opposite hole
                    if row == player:
                        if player == 0:
                            self.state[2][player] += self.state[1][5 - hole]
                            self.state[1][5 - hole] = 0
                        else:
                            self.state[2][player] += self.state[0][5 - hole]
                            self.state[0][5 - hole] = 0
                elif stones > 0:
                    self.state[row][hole] += 1
                    stones -= 1



