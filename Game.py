import random
import time

class Kalaha:

    def __init__(self, init_state = None, starting_player = 0):
        """
        Parameters
        """
        self.board_size = 6
        self.stones = 4

        """
        State and variables
        """
        self.starting_player = starting_player

        if init_state == None:
            self.state = [[self.stones]*self.board_size, [self.stones]*self.board_size, [0,0], self.starting_player]
        else:
            self.state = init_state

        self.player1 = 0
        self.player2 = 1



    def terminal_test(self):
        return sum(self.state[0]) == 0 or sum(self.state[1]) == 0


    def finalize_game(self):
        if sum(self.state[0]) == 0:
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


    def possible_actions(self):
        possible_holes = []
        player = self.state[3]
        for i, hole in enumerate(self.state[player]):
            if hole > 0:
                possible_holes.append(i)
        return possible_holes


    def take(self, hole):
        player = self.state[3]
        stones = self.state[player][hole]
        self.state[player][hole] = 0

        row = player

        # While we still have stones left
        while stones > 0:
            hole += 1

            # If we need to go from one row to the other (at the end of a row)
            if hole == self.board_size:

                # Put stone in players Mancala Store
                self.state[2][row] += 1
                stones -= 1

                if stones == 0 and row != player:
                    self.state[3] = int(not player)

                # Switch Row
                if row == 1:
                    row = 0
                else:
                    row = 1

                # Start from hole 0
                hole = -1


                # If we have stones left -> Put in first hole
                #if stones == 0:
                #    next_player = int(not player)
                #    self.state[3] = next_player



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
                            self.state[3] = int(not player)
                        else:
                            self.state[2][player] += self.state[0][5 - hole]
                            self.state[0][5 - hole] = 0
                            self.state[3] = int(not player)

                elif stones > 0:
                    self.state[row][hole] += 1
                    stones -= 1
                    if stones == 0:
                        self.state[3] = int(not player)




