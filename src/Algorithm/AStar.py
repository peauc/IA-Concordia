from src.Algorithm.IAlgorythm import IAlgorythm
from src.Heuristic.IHeuristics import IHeuristics


class AStar(IAlgorythm):
    def __init__(self, initial_board_state: list, heuristic: IHeuristics):
        super().__init__(initial_board_state, heuristic)

    def compute(self, board):
        pass
