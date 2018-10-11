import abc
from src.node import Node
from src.Heuristic.IHeuristics import IHeuristics
import src.moves as moves

class IAlgorythm:
    _heuristic: IHeuristics
    _current_node: Node
    _is_resolved = False
    _file_name = "default.txt"

    def __init__(self, initial_board_state: list, heuristic: IHeuristics):
        self._current_node = None
        self._open_list = [] + [Node(initial_board_state, initial_board_state.index(0), None, None)]
        self._closed_list = {}
        self._heuristic = heuristic

    """ this method takes a board and its heuristic and compute the best move, then return the actual map state"""
    @abc.abstractmethod
    def compute(self):
        pass

    """ get the output filename """
    def get_file_name(self):
        return self._file_name

    """ To know if the algorithm finished computing"""
    def is_resolved(self) -> bool:
        self._is_resolved = type(self._current_node) is Node and self._current_node.state_map.__eq__(moves.GOAL_STATE)
        return self._is_resolved

    """ print the winning moves """
    def display_winning_path(self):
        good_path = self.get_winning_path()
        print(*good_path, sep='\n')

    def get_debug_infos(self) -> list:
        ret = []

        ret += "Number of room visited: " + str(self._closed_list.__len__()) + '\n'
        if self.is_resolved():
            ret += "Length of the solution: " + str(self.get_winning_path().__len__()) + '\n'
        return ret

    """ Get the winning moves found by the algorythm, throw if algo isn't finished """
    def get_winning_path(self) -> list:
        if not self._is_resolved:
            raise Exception("The game was not completed can't print")
        saved_state = self._current_node
        good_path = [self._current_node]
        while self._current_node.parent_node:
            good_path = [self._current_node.parent_node] + good_path
            self._current_node = self._current_node.parent_node
        self._current_node = saved_state
        return good_path
