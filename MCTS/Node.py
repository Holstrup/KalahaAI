import math
import random
class Node:
    def __init__(self, parent, game_state):
        """Hyper Parameter"""
        self.ee_parameter = 2

        """ Init """
        self.parent = parent
        self.state = game_state
        self.n = 0
        self.r = 0
        self.child_nodes = []

    def rollout(self):
        random_child_state = None
        child_states = self.state.compute_child_states()

        while len(child_states) > 0:
            random_child_state = random.choice(child_states)
            child_states = random_child_state.compute_child_states()

        if random_child_state == None:
            random_child_state = self.state

        random_child_state.finalize_game()
        return random_child_state.evaluate()


    def expand(self):
        if len(self.child_nodes) == 0:
            child_states = self.state.compute_child_states()
            for state in child_states:
                self.child_nodes.append(Node(self, state))

    #def expand(self):
    #    child_states = self.state.compute_child_states()
    #    if len(self.child_nodes) != len(child_states):
    #        selected_state = child_states[len(self.child_nodes)]
    #        self.child_nodes.append(Node(self, selected_state))


    def backpropagate(self, r):
        self.n += 1
        self.r += r
        if self.parent is not None:
            self.parent.backpropagate(r)

    def ucb(self, child):
        if child.n is not 0:
            return child.r / child.n + self.ee_parameter * (math.log(self.n) / child.n)**(1/2)
        else:
            return 10 ** 5

    def isLeaf(self):
        return len(self.child_nodes) == 0
        #if len(self.child_nodes) > 0:
        #    return False
        #else:
            #return len(self.state.compute_child_states()) == 0



