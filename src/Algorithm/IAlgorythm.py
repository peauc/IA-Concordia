import abc


class IAlgorythm:
    __is_resolved = False

    def is_resolved(self) -> bool:
        return self.__is_resolved

    """ this method takes a board and its heuristic and compute the best move, then return the actual map state"""
    @abc.abstractmethod
    def compute(self, board, heuristics) -> list:
        pass


