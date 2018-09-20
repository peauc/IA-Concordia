from moves import move_right
from moves import move_up
from moves import move_left
from moves import move_down
from moves import move_up_right
from moves import move_down_right
from moves import move_up_left
from moves import move_down_left

from node import Node

map_array = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8]

print(map_array)

map_array = move_right(map_array, 1)
print("moved right", map_array)
map_array = move_down(map_array, 2)
print("moved down ", map_array)
map_array = move_up(map_array, 6)
print("moved up   ", map_array)
map_array = move_left(map_array, 2)
print("moved left ", map_array)

a = Node(map_array[:], 1, None)
print("a is: ", a)
b = Node(map_array, 1, None)
print("a == b is: ", a == b)

map_array = move_right(map_array, 1)
print("moved right", map_array)
b = Node(map_array, 2, None)

print("b is: ", map_array)
print("a == b is: ", a == b)
