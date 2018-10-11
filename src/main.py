import random
import src.core as core
from src.Algorithm.DepthFirst import DepthFirst
from src.Algorithm.BreadthFirst import BreadthFirst
from src.Algorithm.BreadthFirstClassical import BreadthFirstClassical
from src.Heuristic.NoHeuristic import NoHeuristic

map_array = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8]

""" TODO: Read from the console for map base state """
def _map_setup() -> list:
    board = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8]
    random.shuffle(board)
    return board


def init_breadth_first(board):
    algo = BreadthFirstClassical(board, NoHeuristic())
    core.loop(algo, board)
    pass


def init_dfs(board):
    algo = DepthFirst(board)
    heuristic = NoHeuristic()
    core.loop(algo, board)


def init_bf(board):
    algo = BreadthFirst(board)
    heuristic = NoHeuristic()
    core.loop(algo, board)


def __main__() -> int:
    board = _map_setup()
    init_breadth_first(board)
    return 0


if __name__ == "__main__":
    __main__()
