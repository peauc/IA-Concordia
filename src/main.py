import src.core as core
import random
from src.Algorithm.DepthFirst import DepthFirst
from src.Heuristic.NoHeuristic import NoHeuristic

map_array = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8]


def _mapSetup() -> list:
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    random.shuffle(board)
    return board


def init_bf():
    board = _mapSetup()
    algo = DepthFirst(board)
    heuristic = NoHeuristic()
    core.loop(algo, heuristic, board)


def __main__() -> int:
    init_bf()
    return 0


if __name__ == "__main__":
    __main__()
