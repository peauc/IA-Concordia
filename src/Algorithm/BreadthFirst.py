from src.Algorithm.IAlgorythm import IAlgorythm
from src.moves import get_children_nodes
from src.moves import is_goal
from src.node import Node


class BreadthFirst(IAlgorythm):

    def compute(self, board, heuristics) -> list:

        while self.__open_list:

            current_node = self.__open_list.pop(0)
            if is_goal(current_node.state_map):
                print("Found goal state ! =>", current_node.__str__())
                return current_node.state_map

            for child in reversed(get_children_nodes(current_node, self.__closed_list, self.__open_list)):

                if child in self.__closed_list:
                    continue

                if child not in self.__open_list:
                    self.__open_list = [child] + self.__open_list

            self.__closed_list.append(current_node)

            # closed_list.append(current_node)
            # next_moves = get_children_nodes(current_node, closed_list, open_list)
            # open_list = next_moves + open_list
            # current_node = open_list.pop(0)
            print("open_list: ", list(map(lambda x: x.__str__(), self.__open_list)), "\n")
            print("closed_list: ", list(map(lambda x: x.__str__(), self.__closed_list)), "\n")
            print("current_node: ", current_node, "\n")
            input()

    def __init__(self, board):
        self.__open_list = [Node(board, board.index(0), None, None)]
        self.__closed_list = []
        pass
