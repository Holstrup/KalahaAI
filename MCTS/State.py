import copy

class State:
    def __init__(self, board_state):
        self.state = board_state
        self.board_size = 6


    def compute_child_states(self):
        child_states = []
        player = self.state[3]
        for i, hole in enumerate(self.state[player]):
            state_copy = copy.deepcopy(self.state)
            if hole > 0:
                state_copy = State(self.take(state_copy, i))
                child_states.append(state_copy)
        return child_states

    def evaluate(self):
        return max(self.state[2][0] - self.state[2][1],0)


    #def evaluate(self):
    #    if self.state[2][0] > self.state[2][1]:
    #        return 1
    #    else:
    #        return 0


    def finalize_game(self):
        if sum(self.state[0]) == 0:
            self.state[2][1] += sum(self.state[1])
            self.state[1] = [0] * self.board_size
        elif sum(self.state[1]) == 0:
            self.state[2][0] += sum(self.state[0])
            self.state[0] = [0] * self.board_size

    def take(self, state, hole):
        player = state[3]
        stones = state[player][hole]
        state[player][hole] = 0

        row = player

        # While we still have stones left
        while stones > 0:
            hole += 1
            # If we need to go from one row to the other (at the end of a row)
            if hole >= self.board_size:

                # Put stone in players Mancala Store
                state[2][row] += 1
                stones -= 1

                if stones == 0 and row != player:
                    state[3] = int(not player)

                # Switch Row
                if row == 1:
                    row = 0
                else:
                    row = 1

                # Start from hole 0
                hole = -1

            else:
                # If 1 stone left and next hole is empty and youre on your own side of the board
                if stones == 1 and state[row][hole] == 0 and row == player:
                    state[row][hole] += 1
                    stones -= 1

                    # Get all stones from opposite hole
                    if row == player:
                        if player == 0:
                            state[2][player] += state[1][self.board_size - 1 - hole]
                            state[1][self.board_size - 1 - hole] = 0
                            state[3] = int(not player)
                        else:
                            state[2][player] += state[0][self.board_size - 1 - hole]
                            state[0][self.board_size - 1 - hole] = 0
                            state[3] = int(not player)

                elif stones > 0:
                    state[row][hole] += 1
                    stones -= 1
                    if stones == 0:
                        state[3] = int(not player)
        return state