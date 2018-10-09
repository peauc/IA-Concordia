import random
import src.Algorithm.IAlgorythm
import src.Heuristic.IHeuristics


def _mapSetup() -> list:
    board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    random.shuffle(board)
    return board


def loop(algo, heuristic):
    board = _mapSetup()
    while not algo.is_resolved():
        print("New computing action from the algorithm")
    pass
