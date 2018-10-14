from src.Algorithm.IAlgorythm import IAlgorythm
from src.Heuristic.IHeuristics import IHeuristics
from src.moves import get_children_nodes
from src.node import Node


class AStar(IAlgorythm):
    def __init__(self, initial_board_state: list, heuristic: IHeuristics):
        super().__init__(initial_board_state, heuristic)

    def _calculate_cost(self, node: Node):
        h = self._heuristic.compute(node.state_map)
        return h + node.depth

    def compute(self):
        while not self.is_resolved():
            if self._open_list.__len__() == 0:
                raise Exception("The algorithm couldn't find the solution")

            self._current_node = self._open_list.pop(0)
            self._closed_list[self._current_node.__hash__()] = self._current_node

            next_moves = get_children_nodes(self._current_node)
            self._open_list = next_moves + self._open_list
            self._open_list.sort(key=lambda element: (self._calculate_cost(element)))
