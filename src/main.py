import src.core as core
from src.Algorithm.BreadthFirst import BreathFirst
from src.Heuristic.NoHeuristic import NoHeuristic

map_array = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8]


def init_bf():
    algo = BreathFirst()
    heuristic = NoHeuristic()
    core.loop(algo, heuristic)


def __main__() -> int:
    init_bf()
    return 0


if __name__ == "__main__":
    __main__()
