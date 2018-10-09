import src.core as core
from src.Algorithm.BreadthFirst import BreathFirst


def initBF():
    algo = BreathFirst()
    if not algo.is_resolved():
        print("initiated correctly")


def main():
    initBF()


if __name__ == "__main__":
    main()
