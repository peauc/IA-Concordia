"""

This file will contain the different functions and constants to interact with the "board".

"""

# Import statements

from src.node import Node

# =========
# CONSTANTS
# =========

# Board dimensions
WIDTH: int = 4
HEIGHT: int = 3
SIZE: int = WIDTH * HEIGHT

# Moves index shift in a single dimension array
MOVE_UP_INDEX_SHIFT: int = -WIDTH
MOVE_DOWN_INDEX_SHIFT: int = WIDTH
MOVE_LEFT_INDEX_SHIFT: int = -1
MOVE_RIGHT_INDEX_SHIFT: int = 1
MOVE_UP_LEFT_INDEX_SHIFT: int = MOVE_UP_INDEX_SHIFT - 1
MOVE_UP_RIGHT_INDEX_SHIFT: int = MOVE_UP_INDEX_SHIFT + 1
MOVE_DOWN_LEFT_INDEX_SHIFT: int = MOVE_DOWN_INDEX_SHIFT - 1
MOVE_DOWN_RIGHT_INDEX_SHIFT: int = MOVE_DOWN_INDEX_SHIFT + 1

# Array containing the possible moves in the order of preference (clock-wise starting from move_up)
MOVES: list = [
    MOVE_UP_INDEX_SHIFT,
    MOVE_UP_RIGHT_INDEX_SHIFT,
    MOVE_RIGHT_INDEX_SHIFT,
    MOVE_DOWN_RIGHT_INDEX_SHIFT,
    MOVE_DOWN_INDEX_SHIFT,
    MOVE_DOWN_LEFT_INDEX_SHIFT,
    MOVE_LEFT_INDEX_SHIFT,
    MOVE_UP_LEFT_INDEX_SHIFT
]

# The goal state our algorithm is trying to reach.
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]


# =========
# FUNCTIONS
# =========

def is_goal(state: list) -> bool:
    return state == GOAL_STATE


def get_children_nodes(node: Node, closed_list: list, open_list: list) -> list:
    """Returns a list of the children nodes of the given node, in order of preference."""

    possible_moves = []
    # closed_states_list = map(lambda closed_list_node: closed_list_node.state_map, closed_list)

    for move in MOVES:
        child: Node = create_child(node, move)

        if child in closed_list and child not in open_list and child is not None:
            possible_moves.append(child)

    print("possible moves:", list(map(lambda x: x.__str__(), possible_moves)), "\n")
    return possible_moves


def can_make_move(position: int, index_shift: int) -> bool:
    """True if the targeted index is in the array bounds."""

    return SIZE > position + index_shift > 0


def create_child(state: Node, move: int) -> Node:
    """Returns a new node for the given move at the given state"""

    if not can_make_move(state.empty_tile_index, move):
        return None

    next_index = state.empty_tile_index + move
    state_map = state.state_map
    state_map[state.empty_tile_index], state_map[next_index] = state_map[next_index], state_map[state.empty_tile_index]

    print("position: ", next_index)
    return Node(state_map[:], next_index, move, state)
