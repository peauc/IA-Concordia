import random
from src.Algorithm.IAlgorythm import IAlgorythm
from src.Heuristic.IHeuristics import IHeuristics


def _mapSetup() -> list:
    board = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8]
    #random.shuffle(board)
    return board


def loop(algo: IAlgorythm, heuristic: IHeuristics):
    board_state = _mapSetup()
    while not algo.is_resolved():
        current_heuristic = heuristic.compute(board_state)
        board_state = algo.compute(board_state, current_heuristic)
        """ Todo: Write to a file """
        print("New computing action from the algorithm")
    pass
