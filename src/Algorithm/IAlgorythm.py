import abc
from src.node import Node

class IAlgorythm:
    __is_resolved = False

    def is_resolved(self) -> bool:
        return self.__is_resolved

    """ this method takes a board and its heuristic and compute the best move, then return the actual map state"""
    @abc.abstractmethod
    def compute(self, board, heuristics) -> list:
        pass

    def __init__(self, initial_board_state : list):
        self._current_node = Node(initial_board_state, initial_board_state.index(0), None, None)
        self._open_list = []
        self._closed_list = []
