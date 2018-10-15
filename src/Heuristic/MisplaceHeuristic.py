from src.Heuristic.IHeuristics import IHeuristics
from src.moves import *


class MisplaceHeuristic(IHeuristics):
    """
    This simple heuristic just adds one point to the score for each misplaced tile.
    """

    def __init__(self):
        pass

    def compute(self, board) -> int:
        total_node_score = 0

        for index, tile in enumerate(board):
            goal_index = GOAL_STATE.index(tile)
            if goal_index != index:
                total_node_score += 1

        return total_node_score
