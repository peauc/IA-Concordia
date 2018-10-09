import src.core as core
from src.Algorithm.BreadthFirst import BreathFirst
from src.Heuristic.NoHeuristic import NoHeuristic
from src.moves import get_children_nodes
from src.node import Node

map_array = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]


def init_bf():
    algo = BreathFirst()
    heuristic = NoHeuristic()
    core.loop(algo, heuristic)


def is_goal(state: Node):
    """True if the given state is the goal state"""
    return state.state_map == goal_state


def depth_first_search(initial_state: list):
    """Performs a depth first search algorithm from the given state"""

    current_node = Node(initial_state, initial_state.index(0), None, None)
    open_list = []
    closed_list = []
    while not is_goal(current_node):
        closed_list.append(current_node)
        next_moves = get_children_nodes(current_node, closed_list, open_list)
        open_list = next_moves + open_list
        current_node = open_list.pop(0)
        print("open_list: ", list(map(lambda x: x.__str__(), open_list)), "\n")
        print("closed_list: ", list(map(lambda x: x.__str__(), closed_list)), "\n")
        print("current_node: ", current_node, "\n")
        input()


def __main__() -> int:
    depth_first_search(map_array)
    return 0


if __name__ == "__main__":
    __main__()
