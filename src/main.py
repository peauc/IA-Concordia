import src.core as core
from src.Algorithm.BreadthFirst import BreathFirst
from src.Algorithm.IAlgorythm import IAlgorythm


def initBF():
    algo = BreathFirst()
    if not algo.is_resolved():
        print("initiated correctly")
    core.loop(algo, None)

def main():
    initBF()


if __name__ == "__main__":
    main()
