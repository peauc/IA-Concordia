import src.moves
import src.node
import random


def _mapSetup() -> list:
    board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    random.shuffle(board)
    return board


def main():
    board = _mapSetup()

    print("Main")


if __name__ == "__main__":
    main()
