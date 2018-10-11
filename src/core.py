from src.Algorithm.IAlgorythm import IAlgorythm
from src.Heuristic.IHeuristics import IHeuristics


def loop(algo: IAlgorythm, heuristic: IHeuristics, board_state: list):
    while not algo.is_resolved():
        board_state = algo.compute(board_state, None)
        """ Todo: Write to a file """
        print("New computing action from the algorithm")
    algo.display_winning_path()
