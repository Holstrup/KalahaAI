

class AI:
    def __init__(self,depth):
        self.game=None
        self.best_move = {}
        self.depth = depth

    def get_best_move(self,game,state,maximizing_player,pruning):

        self.game = game
        self.minimax(state,maximizing_player,self.depth,float("-inf"),float("inf"),pruning)

        if self.depth == 0:
            return 0
        else:
            return self.best_move[self.depth]

    def evaluate(self, state):
        return state[2][self.game.player2] - state[2][self.game.player1]

    def minimax(self, state, maximizing_player,depth,alpha,beta,pruning):

        if self.game.terminal_test(state):
            self.game.finalize_game(state=state)
            return self.evaluate(state)

        elif depth == 0:

            return self.evaluate(state)

        elif maximizing_player:

            best_val = float("-inf")

            moves = self.game.possible_actions(self.game.player2,state)


            for move in moves:

                new_state, go_again = self.game.take(self.game.player2,move,state)

                val = self.minimax(new_state, go_again, depth - 1,alpha,beta,pruning)

                if val>best_val:
                    self.best_move[depth] = move
                best_val = max(best_val, val)

                alpha = max(alpha, best_val)

                if beta <= alpha and pruning:

                    break
            return best_val

        elif not maximizing_player:

            best_val = float("inf")

            moves = self.game.possible_actions(self.game.player1, state)

            for move in moves:

                new_state, go_again = self.game.take(self.game.player1, move, state)

                val = self.minimax(new_state, not go_again, depth - 1,alpha,beta,pruning)

                if val<best_val:
                    self.best_move[depth] = move
                best_val = min(best_val, val)

                beta = min(beta, best_val)

                if beta <= alpha and pruning:

                    break

            return best_val



