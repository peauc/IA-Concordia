class MoveError(Exception):

    """
    Attributes:
        mapState -- State of the map on which it failed
        move -- tried move that failed
    """

    def __init__(self, map_state, move):
        self.expression = map_state
        self.message = move

