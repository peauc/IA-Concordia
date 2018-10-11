import random
import src.core as core
from src.Algorithm.DepthFirst import DepthFirst
from src.Algorithm.BreadthFirst import BreadthFirst
from src.Algorithm.BreadthFirstClassical import BreadthFirstClassical
from src.Heuristic.NoHeuristic import NoHeuristic
from src.Algorithm.IAlgorythm import IAlgorythm

ConcordiaExemple = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8]

""" TODO: Read from the console for map base state """
def _map_setup() -> list:
    board = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8]
    random.shuffle(board)
    return board


def init_breadth_first(board: list) -> IAlgorythm:
    algo = BreadthFirstClassical(ConcordiaExemple, NoHeuristic())
    return algo


def init_dfs(board) -> IAlgorythm:
    algo = DepthFirst(board, NoHeuristic())
    return algo


def init_bf(board) -> IAlgorythm:
    algo = BreadthFirst(board)
    return algo


def __main__() -> int:
    algo_list = [
            init_breadth_first(board=_map_setup()),
            init_dfs(board=_map_setup()),
        ]

    """ Will fire every algorithm enqueued """
    for algo in algo_list:
        core.logic(algo)
    return 0


if __name__ == "__main__":
    __main__()
