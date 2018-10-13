import random
import src.core as core
from src.Algorithm.AStar import AStar
from src.Algorithm.BestFirst import BestFirst
from src.Algorithm.DepthFirst import DepthFirst
from src.Algorithm.BreadthFirst import BreadthFirst
from src.Heuristic.DistanceHeuristic import DistanceHeuristic
from src.Heuristic.NoHeuristic import NoHeuristic
from src.Algorithm.IAlgorythm import IAlgorythm
from src.Heuristic.MisplaceHeuristic import MisplaceHeuristic

ConcordiaExample = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8]


def _map_setup() -> list:
    """ TODO: Read from the console for map base state """
    board = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8]
    #random.shuffle(board)
    return board


def init_breadth_first(board: list) -> IAlgorythm:
    algo = BreadthFirst(board, NoHeuristic())
    return algo


def init_astar(board: list) -> IAlgorythm:
    algo = AStar(board, DistanceHeuristic())
    return algo


def init_dfs(board) -> IAlgorythm:
    algo = DepthFirst(board, NoHeuristic())
    return algo


def init_bfs(board) -> IAlgorythm:
    algo = BestFirst(board, DistanceHeuristic())
    return algo


def __main__() -> int:
    algo_list = [
            #init_breadth_first(board=_map_setup()),
            #init_dfs(board=_map_setup()),
            #init_bfs(board=_map_setup()),
            init_astar(board=_map_setup())
        ]

    """ Will fire every algorithm enqueued """
    for algo in algo_list:
        core.logic(algo)
    return 0


if __name__ == "__main__":
    __main__()
