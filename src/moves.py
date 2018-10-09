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

# Associates a string to each move describing it, for debugging purpose.
MOVES_STRING_REPRESENTATION_MAP: map = {
    MOVE_UP_INDEX_SHIFT: "UP",
    MOVE_UP_RIGHT_INDEX_SHIFT: "UP_RIGHT",
    MOVE_RIGHT_INDEX_SHIFT: "RIGHT",
    MOVE_DOWN_RIGHT_INDEX_SHIFT: "DOWN_RIGHT",
    MOVE_DOWN_INDEX_SHIFT: "DOWN",
    MOVE_DOWN_LEFT_INDEX_SHIFT: "DOWN_LEFT",
    MOVE_LEFT_INDEX_SHIFT: "LEFT",
    MOVE_UP_LEFT_INDEX_SHIFT: "UP_LEFT"
}

# The goal state our algorithm is trying to reach.
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]


# =========
# FUNCTIONS
# =========

def is_goal(state: list) -> bool:
    """True if the given board is equal to the goal state, false otherwise."""

    return state == GOAL_STATE


def get_children_nodes(node: Node, closed_list: list, open_list: list) -> list:
    """Returns a list of the children nodes of the given node, in order of preference."""

    possible_moves = []
    # closed_states_list = map(lambda closed_list_node: closed_list_node.state_map, closed_list)

    for move in MOVES:
        child: Node = create_child(node, move)

        if child is not None:
            possible_moves.append(child)

    # print("index is:", node.empty_tile_index)
    # print("possible moves:", list(map(lambda x: x.__str__(), possible_moves)), "\n")
    return possible_moves


def can_make_move(position: int, index_shift: int) -> bool:
    """True if the targeted index is in the array bounds."""

    return SIZE > position + index_shift >= 0


def create_child(state: Node, move: int) -> Node:
    """Returns a new node for the given move at the given state"""

    if not can_make_move(state.empty_tile_index, move):
        return None

    # print("create child for move:", MOVES_STRING_REPRESENTATION_MAP[move])
    next_index = state.empty_tile_index + move
    # print("index:", state.empty_tile_index, " next_index:", next_index)
    state_map = state.state_map[:]
    state_map[state.empty_tile_index], state_map[next_index] = state_map[next_index], state_map[state.empty_tile_index]

    # print("position: ", next_index)
    return Node(state_map, next_index, move, state)
