from Game import Kalaha
import copy
import numpy as np


class Agent:
    def __init__(self):
        self.search_depth = 4

    def evaluate(self, state):
        """
        :param state: Game State
        :return: Evaluated score based on heuristic
        """
        return state[2][0] - state[2][1]

    def children(self, curr_game):
        """
        :param curr_game: Game State
        :return: All 'children' game states after all possible moves.
        """
        M = curr_game.possible_actions()
        child_games = []
        for move in M:
            game_state_copy = copy.deepcopy(curr_game.state)
            new_game = Kalaha(init_state=game_state_copy)
            new_game.take(move)
            child_games.append(new_game)
        return child_games

    def minimax(self, game, depth):
        player = game.state[3]

        if game.terminal_test() or depth == 0:
            return None, self.evaluate(game.state)

        # Max Player
        elif player == 0:
            child_games = self.children(game)
            values = np.zeros(len(child_games), dtype=int)
            for i, child in enumerate(child_games):

                _, value = self.minimax(child, depth - 1)
                values[i] = value

            best_value = np.max(values)
            best_move = game.possible_actions()[np.argmax(values)]
            return best_move, best_value

        # Min Player
        elif player == 1:
            child_games = self.children(game)
            values = np.zeros(len(child_games), dtype=int)
            for i, child in enumerate(child_games):

                _, value = self.minimax(child, depth - 1)
                values[i] = value

            best_value = np.min(values)
            best_move = game.possible_actions()[np.argmin(values)]
            return best_move, best_value

    def minimax_ab(self, game, depth, alpha=-100, beta=100):
        player = game.state[3]

        if game.terminal_test() or depth == 0:
            return None, self.evaluate(game.state)

        # Max Player
        elif player == 0:
            moves = game.possible_actions()
            child_games = self.children(game)

            best_value = -100
            best_move = None

            for i, child in enumerate(child_games):

                _, value = self.minimax_ab(child, depth - 1, alpha=alpha, beta=beta)
                best_value = max(best_value, value)
                if best_value > alpha:
                    alpha = best_value
                    best_move = moves[i]

                if beta <= alpha:
                    break

            return best_move, best_value

        # Min Player
        elif player == 1:
            moves = game.possible_actions()
            child_games = self.children(game)

            best_value = 100
            best_move = None

            for i, child in enumerate(child_games):

                move, value = self.minimax_ab(child, depth - 1, alpha=alpha, beta=beta)
                best_value = min(best_value, value)
                if best_value < beta:
                    beta = best_value
                    best_move = moves[i]

                if beta <= alpha:
                    break

            return best_move, best_value

    def find_next_move(self, game, pruning=True):
        if pruning:
            next_move, _ = self.minimax_ab(game, self.search_depth)
        else:
            next_move, _ = self.minimax(game, self.search_depth)
        return next_move
