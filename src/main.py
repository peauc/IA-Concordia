import src.core as core
import random
from src.Algorithm.DepthFirst import DepthFirst
from src.Algorithm.BreadthFirst import BreadthFirst
from src.Heuristic.NoHeuristic import NoHeuristic

map_array = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8]


def _mapSetup() -> list:
    board = [1, 2, 3, 4, 5, 6, 0, 8, 9, 10, 11, 7]
    #random.shuffle(board)
    return board


def _print(filename, array):
    with open(filename, 'w') as f:
        for item in array:
            f.write("%s\n" % item)


def init_dfs():
    board = _mapSetup()
    algo = DepthFirst(board)
    heuristic = NoHeuristic()
    core.loop(algo, heuristic, board)
    winning_path = algo.get_winning_path()
    _print(algo.get_file_name(), winning_path)

def init_bf():
    board = _mapSetup()
    algo = BreadthFirst(board)
    heuristic = NoHeuristic()
    core.loop(algo, heuristic, board)


def __main__() -> int:
    init_dfs()
    return 0


if __name__ == "__main__":
    __main__()
