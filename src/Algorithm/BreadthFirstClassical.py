from src.Algorithm.IAlgorythm import IAlgorythm
from src.moves import get_children_nodes
from src.Heuristic.IHeuristics import IHeuristics


class BreadthFirstClassical(IAlgorythm):
    def __init__(self, initial_board_state: list, heuristic: IHeuristics):
        super().__init__(initial_board_state, heuristic)
        self._file_name = "BreadthFirst.txt"

    def compute(self):
        while not self.is_resolved():
            if self._open_list.__len__() == 0:
                raise Exception("The algorithm couldn't find the solution")

            self._current_node = self._open_list.pop(0)
            self._closed_list[self._current_node.__hash__()] = self._current_node

            next_moves = get_children_nodes(self._current_node, self._closed_list, self._open_list)
            for x in list(next_moves):
                if x.__hash__() in self._closed_list:
                        next_moves.remove(x)
            self._open_list += next_moves
