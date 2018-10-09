from src.Heuristic.IHeuristics import IHeuristics


class NoHeuristic(IHeuristics):
    def __init__(self):
        pass

    def compute(self, board) -> list:
        return []
