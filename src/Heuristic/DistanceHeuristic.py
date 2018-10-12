from math import *
from src.Heuristic.IHeuristics import IHeuristics
from src.moves import *


class DistanceHeuristic(IHeuristics):
    """
    This simple heuristic takes for each tile the distance between its actual and the position it should be at.
    """

    def __init__(self):
        pass

    def compute(self, board) -> int:
        total_node_score = 0

        for index, tile in enumerate(board):
            x_index = index % WIDTH
            y_index = floor(index / WIDTH)

            goal_index = GOAL_STATE.index(tile)
            x_goal_index = goal_index % WIDTH
            y_goal_index = floor(goal_index / WIDTH)

            distance = floor(sqrt(pow(x_goal_index - x_index, 2) + pow(y_goal_index - y_index, 2)))
            total_node_score += distance
        return total_node_score
