import random
from src.Algorithm.IAlgorythm import IAlgorythm
from src.Heuristic.IHeuristics import IHeuristics


def _mapSetup() -> list:
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    random.shuffle(board)
    return board


def loop(algo: IAlgorythm, heuristic: IHeuristics):
    board_state = _mapSetup()
    while not algo.is_resolved():
        current_heuristic = heuristic.compute(board_state)
        board_state = algo.compute(board_state, current_heuristic)
        """ Todo: Write to a file """
        print("New computing action from the algorithm")
    pass
