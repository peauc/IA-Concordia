from moves import move_right, move_up, move_left, move_down, move_up_right, move_down_right, move_up_left, move_down_left

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
