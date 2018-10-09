

INDEX_POSITION_MAPPING = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']


class Node:

    """
    Describes a node. Contains the current state, the move made to arrive to this node,
    the position of the empty tile,and the parent of this node.
    """

    # Private

    __empty_tile_name: str = '0'

    # Public

    state_map = []
    move = None
    empty_tile_index: int = 0
    parent_node: object = None

    def __init__(self, state_map: list, empty_tile_position: int, move: int, parent: object) -> None:
        super().__init__()
        self.state_map = state_map
        self.empty_tile_index = empty_tile_position
        self.__empty_tile_name= INDEX_POSITION_MAPPING[empty_tile_position]
        self.parent_node = parent
        self.move = move
        self.depth = 0
        if type(parent) is Node:
            self.depth = parent.depth + 1

    def __str__(self) -> str:
        return self.__empty_tile_name + " [" + ", ".join(str(e) for e in self.state_map) + "]"

    def __hash__(self):
        return "".join(str(e) for e in self.state_map)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return o.state_map == self.state_map
        return False
