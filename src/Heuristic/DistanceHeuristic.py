from src.Heuristic import IHeuristics
from src.moves import *


class DistanceHeuristic(IHeuristics):
    """
    This simple heuristic takes for each tile the distance between its actual and the position it should be at.
    """

    def __init__(self):
        pass

    def compute(self, board) -> int:
        for index, tile in enumerate(board):
            x_index = index % WIDTH
            y_index = floor(index / WIDTH)
        return 1
