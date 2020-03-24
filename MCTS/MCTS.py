from MCTS.State import State
from MCTS.Node import Node
import numpy as np


import time
class MCTS:
    def __init__(self, init_state=None):
        self.starting_player = 0

        if init_state is None:
            root = [[4] * 6, [4] * 6, [0, 0]] + [self.starting_player]
            self.inital_state = State(root)
        else:
            self.inital_state = init_state

        self.root_node = Node(parent=None, game_state=self.inital_state)


    def tree_policy(self, node):
        current_node = node
        while not current_node.state.is_terminal_state():
            if not current_node.is_fully_expanded():
                return current_node.expand()
            else:
                current_node = self.most_promising_child(current_node)
        return current_node

    def MCTS(self, n0):
        n1 = self.tree_policy(n0)
        reward = n1.rollout()
        n1.backpropagate(reward)

    def most_promising_child(self, current_node):
        max_ucb = 0
        max_child = None
        for child in current_node.child_nodes:
            ucb_cur = current_node.ucb(child)
            if ucb_cur > max_ucb:
                max_ucb = ucb_cur
                max_child = child
        return max_child

    """ Helper Functions """
    def depth(self, node):
        if len(node.child_nodes) == 0:
            return 1
        else:
            depths = []
            for child in node.child_nodes:
                depths.append(self.depth(child))
            return max(depths) + 1

    def noNodes(self, node):
        if len(node.child_nodes) == 0:
            return 1
        else:
            nodes = []
            for child in node.child_nodes:
                nodes.append(self.no_nodes(child))
            return sum(nodes) + 1

    def max_path(self, node, states):
        states.append(node.state.state)
        child = self.most_promising_child(node)
        if child == None:
            return states
        else:
            return self.max_path(child, states)

    def robust_child(self):
        hole, most_visits = None, 0
        for i, child in enumerate(self.root_node.child_nodes):
            if child.n > most_visits:
                most_visited_child = child
                most_visits = child.n
                hole = i
        return hole, most_visited_child

"""

# 1
print("MOVE 1")
mcts = MCTS()
start_time = time.time()
while time.time() - start_time < 30:
    s0 = mcts.root_node
    mcts.MCTS(s0)


print("\n")
for child in mcts.root_node.child_nodes:
    print(mcts.root_node.ucb(child), child.n, child.r, child.state.state)
print("\n")

print("Max depth is {}".format(mcts.depth(mcts.root_node)))
print("Nodes explored: {}".format(mcts.no_nodes(mcts.root_node)))

state_path = mcts.max_path(mcts.root_node, [])

move = np.argmin(np.array(state_path[1][0]))
robust_child, child = mcts.robust_child()
print("Max Child: {}".format(move))
print("Robust Child: {}".format(robust_child))


print("\nState Path")
for i, state in enumerate(state_path):
    print(i, state)


# 2
print("MOVE 2")
mcts = MCTS(init_state=child.state)
start_time = time.time()
print(mcts.root_node.state.state)
while time.time() - start_time < 30:
    s0 = mcts.root_node
    mcts.MCTS(s0)


print("\n")
for child in mcts.root_node.child_nodes:
    print(mcts.root_node.ucb(child), child.n, child.r, child.state.state)
print("\n")

print("Max depth is {}".format(mcts.depth(mcts.root_node)))
print("Nodes explored: {}".format(mcts.no_nodes(mcts.root_node)))

state_path = mcts.max_path(mcts.root_node, [])

move = np.argmin(np.array(state_path[1][0]))
robust_child, child = mcts.robust_child()
print("Max Child: {}".format(move))
print("Robust Child: {}".format(robust_child))



print("\nState Path")
for i, state in enumerate(state_path):
    print(i, state)


"""



