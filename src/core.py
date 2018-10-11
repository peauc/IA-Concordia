from src.Algorithm.IAlgorythm import IAlgorythm
from src.Heuristic.IHeuristics import IHeuristics


def loop(algo: IAlgorythm, heuristic: IHeuristics, board_state: list):
    while not algo.is_resolved():
        current_heuristic = heuristic.compute(board_state)
        board_state = algo.compute(board_state, current_heuristic)
        """ Todo: Write to a file """
        print("New computing action from the algorithm")
    algo.display_winning_path()
