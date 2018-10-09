import abc


class IHeuristics:
    """this method takes a board state as first parameter compute the move's heuristics and return it as a list """
    @abc.abstractmethod
    def compute(self, board) -> list:
        pass


