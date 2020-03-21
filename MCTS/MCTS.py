from State import State
from Node import Node
import time
class MCTS:
    def __init__(self):
        self.starting_player = 0
        init_board = [[4] * 6, [4] * 6, [0, 0], self.starting_player]
        self.inital_state = State(init_board)
        self.root_node = Node(parent=None, game_state=self.inital_state)


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
                nodes.append(self.noNodes(child))
            return len(nodes) + 1

    def tree_policy(self, node):
        2+2


    def most_promising_child(self, current_node):
        max_ucb = 0
        max_child = None
        for child in current_node.child_nodes:
            ucb_cur = current_node.ucb(child)
            if ucb_cur > max_ucb:
                max_ucb = ucb_cur
                max_child = child
        return max_child

    def main(self):
        current = self.root_node
        print(current.n, current.r)
        while not current.isLeaf():
            current = self.most_promising_child(current)
        print(current.state.state)

        if current.n > 0:
            current.expand()
            if len(current.child_nodes) > 0:
                current = current.child_nodes[0]

        r_score = current.rollout()
        current.backpropagate(r_score)





mcts = MCTS()
start_time = time.time()

while time.time() - start_time < 2:
    mcts.main()


for child in mcts.root_node.child_nodes:
    print(mcts.root_node.ucb(child), child.n, child.r, child.state.state)


print(mcts.depth(mcts.root_node))