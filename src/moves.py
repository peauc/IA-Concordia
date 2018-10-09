import src.Exceptions


WIDTH = 4
HEIGHT = 3
SIZE = WIDTH * HEIGHT


def move_up(map_array, pos):
    if pos - WIDTH < 0:
        raise src.Exceptions.MoveError(map_array, 'move_up')
    map_array[pos - WIDTH], map_array[pos] = map_array[pos], map_array[pos - WIDTH]
    return map_array


def move_down(map_array, pos):
    if pos + WIDTH > SIZE - 1:
        raise src.Exceptions.MoveError(map_array, 'move_down')

    map_array[pos + WIDTH], map_array[pos] = map_array[pos], map_array[pos + WIDTH]
    return map_array


def move_left(map_array, pos):
    if pos - 1 < 0:
        raise src.Exceptions.MoveError(map_array, 'move_left')

    map_array[pos - 1], map_array[pos] = map_array[pos], map_array[pos - 1]
    return map_array


def move_right(map_array, pos):
    if pos + 1 > SIZE - 1:
        raise src.Exceptions.MoveError(map_array, 'move_right')

    map_array[pos + 1], map_array[pos] = map_array[pos], map_array[pos + 1]
    return map_array


def move_up_left(map_array, pos):
    if pos - WIDTH - 1 < 0:
        raise src.Exceptions.MoveError(map_array, 'move_up_left')

    map_array[pos - WIDTH - 1], map_array[pos] = map_array[pos], map_array[pos - WIDTH - 1]
    return map_array


def move_down_left(map_array, pos):
    if pos + WIDTH - 1 > SIZE - 1:
        raise src.Exceptions.MoveError(map_array, 'move_down_left')

    map_array[pos + WIDTH - 1], map_array[pos] = map_array[pos], map_array[pos + WIDTH - 1]
    return map_array


def move_up_right(map_array, pos):
    if pos - WIDTH + 1 < 0:
        raise src.Exceptions.MoveError(map_array, 'move_up_right')

    map_array[pos - WIDTH + 1], map_array[pos] = map_array[pos], map_array[pos - WIDTH + 1]
    return map_array


def move_down_right(map_array, pos):
    if pos + WIDTH + 1 > SIZE - 1:
        raise src.Exceptions.MoveError(map_array, 'move_down_right')

    map_array[pos + WIDTH + 1], map_array[pos] = map_array[pos], map_array[pos + WIDTH + 1]
    return map_array
