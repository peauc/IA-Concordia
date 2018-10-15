import random
import src.core as core
from src.Algorithm.AStar import AStar
from src.Algorithm.BestFirst import BestFirst
from src.Algorithm.DepthFirst import DepthFirst
from src.Algorithm.BreadthFirst import BreadthFirst
from src.Heuristic.DistanceHeuristic import DistanceHeuristic
from src.Heuristic.NoHeuristic import NoHeuristic
from src.Heuristic.IHeuristics import IHeuristics
from src.Algorithm.IAlgorythm import IAlgorythm
from src.Algorithm.IterativeDepthFirst import IterativeDepthFirst
from src.Heuristic.MisplaceHeuristic import MisplaceHeuristic

ConcordiaExample = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8]


def _map_setup() -> list:
    """ TODO: Read from the console for map base state """
    board = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8]
    random.shuffle(board)
    return board


def init_breadth_first(board, heuristics: IHeuristics, file_name) -> IAlgorythm:
    algo = BreadthFirst(board, heuristics)
    algo.set_file_name(file_name)
    return algo


def init_astar(board, heuristics: IHeuristics, file_name) -> IAlgorythm:
    algo = AStar(board, heuristics)
    algo.set_file_name(file_name)
    return algo


def init_dfs(board, heuristics: IHeuristics, file_name) -> IAlgorythm:
    algo = DepthFirst(board, heuristics)
    algo.set_file_name(file_name)
    return algo


def init_idfs(board, heuristics: IHeuristics,file_name) -> IAlgorythm:
    algo = IterativeDepthFirst(board, heuristics)
    algo.set_file_name(file_name)
    return algo


def init_bfs(board, heuristics: IHeuristics, file_name) -> IAlgorythm:
    algo = BestFirst(board, heuristics)
    algo.set_file_name(file_name)
    return algo


def _verify_input(string):
    if len(string) != 12:
        raise Exception("Bad format of map")
    if len(string) != len(set(string)):
        raise Exception("You put some duplicate in the map")
    if int(max(string)) > 11:
        raise Exception("Only numbers allowed are from 0 to 11 included")


def __main__() -> int:
    user_input = input("Please type an map state, exemple for the completed map:\n1 2 3 4 5 6 7 8 9 10 11 0\n")
    user_input = [int(i) for i in user_input.split()]
    try:
        _verify_input(user_input)
    except Exception as e:
        print(e.__str__())
        return 1

    print("If you want to cancel a running algorithm, press ctrl + c it will fire the next one automatically ")
    algo_list = [
            init_dfs(board=user_input, heuristics=NoHeuristic(), file_name="puzzleDFS.txt"),
            #init_idfs(board=user_input, heuristics=NoHeuristic(), file_name="puzzleIDFS.txt"),
            init_bfs(board=user_input, heuristics=MisplaceHeuristic(), file_name="puzzleBFS-h1.txt"),
            init_bfs(board=user_input, heuristics=DistanceHeuristic(), file_name="puzzleBFS-h2.txt"),
            init_astar(board=user_input, heuristics=MisplaceHeuristic(), file_name="puzzleAs-h1.txt"),
            init_astar(board=user_input, heuristics=DistanceHeuristic(), file_name="puzzleAs-h2.txt"),
        ]

    """ Will fire every algorithm enqueued """
    for algo in algo_list:
        core.logic(algo)
    return 0


if __name__ == "__main__":
    __main__()
