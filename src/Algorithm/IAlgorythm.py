import abc
from src.node import Node
import src.moves as moves

class IAlgorythm:
    _current_node: Node
    _is_resolved = False

    def is_resolved(self) -> bool:
        self._is_resolved = type(self._current_node) is Node and self._current_node.state_map.__eq__(moves.GOAL_STATE)
        return self._is_resolved

    """ this method takes a board and its heuristic and compute the best move, then return the actual map state"""
    @abc.abstractmethod
    def compute(self, board, heuristics) -> list:
        pass

    def __init__(self, initial_board_state : list):
        self._current_node = None
        self._open_list = [] + [Node(initial_board_state, initial_board_state.index(0), None, None)]
        self._closed_list = {}

    def display_winning_path(self):
        if not self._is_resolved:
            raise Exception("The game was not completed can't print")
        good_path = [self._current_node]
        while self._current_node.parent_node:
            good_path = [self._current_node.parent_node] + good_path
            self._current_node = self._current_node.parent_node
        print(*good_path, sep='\n')
