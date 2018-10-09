from src.Algorithm.IAlgorythm import IAlgorythm
from src.moves import get_children_nodes
from src.moves import is_goal
from src.node import Node


class BreathFirst(IAlgorythm):

    def compute(self, board, heuristics) -> list:
        current_node = Node(board, board.index(0), None, None)
        open_list = []
        closed_list = []
        while not is_goal(current_node):
            closed_list.append(current_node)
            next_moves = get_children_nodes(current_node, closed_list, open_list)
            open_list = next_moves + open_list
            current_node = open_list.pop(0)
            print("open_list: ", list(map(lambda x: x.__str__(), open_list)), "\n")
            print("closed_list: ", list(map(lambda x: x.__str__(), closed_list)), "\n")
            print("current_node: ", current_node, "\n")
            input()

    def __init__(self, initial_board_state: list):
        super(BreathFirst, self).__init__(initial_board_state)
        pass
