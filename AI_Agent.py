

class AI:
    def __init__(self,depth,eval_store,eval_side,eval_empty):
        self.game=None
        self.best_move = {}
        self.depth = depth
        self.eval_store=eval_store
        self.eval_side = eval_side
        self.eval_empty = eval_empty

    def get_best_move(self,game,state,maximizing_player,pruning):

        self.game = game
        self.minimax(state,maximizing_player,self.depth,float("-inf"),float("inf"),pruning)

        if self.depth == 0:
            return 0
        else:
            return self.best_move[self.depth]

    def evaluate(self, state):
        return state[2][1] - state[2][0]

    def complex_evaluate(self, state,max_player):
        """
        :param state: Game State
        :return: Evaluated score based on factor-based heuristic
        """
        if max_player:
            player = 1
        else:
            player =0
        eval_score = 0

        # Add stones in stores comparison
        if self.eval_store:
            eval_score += self.compare_stores(state)

        # Add stones on sides comparison
        if self.eval_side:
            eval_score += self.compare_sides(state,player)

        # Add empty hole comparison
        if self.eval_empty:
            eval_score += self.compare_empty_holes(state)

        return eval_score

    def compare_stores(self,state):
        """
        :param state: Game State
        :return: Number of stones in player 2's store minus number of stones in store of player 1
        """
        return state[2][self.game.player2] - state[2][self.game.player1]

    def compare_sides(self,state,player):
        """
        :param state: Game State
        :return: Number representing a comparison of total number of stones on each side
        """
        side_player = sum(state[player])
        total = sum(state[0]+state[1])


        if side_player> total/2:
            if player ==0:
            #return 0.75 since more stones is not as good as a stone in the store
                return -0.75
            else:
                return 0.75
        else :# if equal amount of stones
            return 0

    def compare_empty_holes(self,state,stones=4):
        """
        :param state: Game State, stones setting threshold of when an opposite hole is "valuable"
        :return: number representing comparison of empty holes on each side
        """
        empty_holes_1 = [hole for hole,stones in enumerate(state[0]) if stones == 0]
        empty_holes_2 = [hole for hole,stones in enumerate(state[1]) if stones == 0]

        score = 0

        stone_threshold = stones #number representing threshold of stones

           #first increment score as player 1
        for empty_hole in empty_holes_1:
            score -= 0.1
             #if opposite hole contains more than the threshold, an extra value is added
            if state[1][empty_hole] >= stone_threshold:
                score -= 0.05

            # first decrement score as player 2
        for empty_hole in empty_holes_2:
            score += 0.1
            # if opposite hole contains more than the threshold, an extra value is added
            if state[0][empty_hole] >= stone_threshold:
                score += 0.05

        return score

    def minimax(self, state, maximizing_player,depth,alpha,beta,pruning):

        if self.game.terminal_test(state):
            self.game.finalize_game(state=state)
            return self.complex_evaluate(state,maximizing_player)

        elif depth == 0:

            return self.complex_evaluate(state,maximizing_player)

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



