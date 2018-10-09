INDEX_POSITION_MAPPING = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']


class Node:

    __map_state = []
    __empty_tile_position = 0
    __empty_tile_index = '0'
    __parent_node = None

    def __init__(self, map_state, empty_tile_position, parent) -> None:
        super().__init__()
        self.__map_state = map_state
        self.__empty_tile_position = empty_tile_position
        self.__empty_tile_index = INDEX_POSITION_MAPPING[empty_tile_position]
        self.__parent_node = parent

    def __str__(self) -> str:
        return self.__empty_tile_index + " [" + ", ".join(str(e) for e in self.__map_state) + "]"

    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return o.__map_state == self.__map_state
        return False
