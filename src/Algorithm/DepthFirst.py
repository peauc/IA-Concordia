from src.Algorithm.IAlgorythm import IAlgorythm
from src.moves import get_children_nodes
from src.moves import is_goal
from src.node import Node


class DepthFirst(IAlgorythm):

    def compute(self, board, heuristics) -> list:
        self._current_node = self._open_list.pop(0)
        self._closed_list.append(self._current_node)

        next_moves = get_children_nodes(self._current_node, self._closed_list, self._open_list)
        self._open_list = next_moves + self._open_list
        self.__str__()
        input()

    def __str__(self):
        print("open_list: ", list(map(lambda x: x.__str__(), self._open_list)), "\n")
        print("closed_list: ", list(map(lambda x: x.__str__(), self._closed_list)), "\n")
        print("current_node: ", self._current_node, "\n")

    def __init__(self, initial_board_state: list):
        super(DepthFirst, self).__init__(initial_board_state)
        pass
