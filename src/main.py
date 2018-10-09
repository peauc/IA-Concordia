import src.core as core
from src.Algorithm.BreadthFirst import BreathFirst
from src.Heuristic.NoHeuristic import NoHeuristic
from src.Algorithm.IAlgorythm import IAlgorythm


def init_bf():
    algo = BreathFirst()
    heuristic = NoHeuristic()
    core.loop(algo, heuristic)


def main():
    init_bf()


if __name__ == "__main__":
    main()
