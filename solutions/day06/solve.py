
from custom_types import Grid
from utils import parse_grid

type Location = tuple[int, int]


DIRECTIONS = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

TURNS = ['^', '>', 'v', '<']


def turn_right(dir: str):
    index = TURNS.index(dir)
    new_index = None
    if index == 3:
        new_index = 0
    else:
        new_index = index + 1
    return TURNS[new_index]


def in_bounds(position: Location, grid: Grid) -> bool:
    r, c = position
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def move(position: Location, direction: str) -> Location:
    r, c = position
    row_step, col_step = DIRECTIONS[direction]
    return r + row_step, c + col_step


def solve(data: str):
    start = (0, 0)
    direction = ""
    grid = parse_grid(data)
    for r, row in enumerate(grid):
        for c, location in enumerate(row):
            if location in DIRECTIONS:
                start = (r, c)
                direction = location

    visited: set[Location] = set()
    position = start
    visited.add(start)

    while True:
        next_position = move(position, direction)

        if not in_bounds(next_position, grid):
            break

        r, c = next_position
        if grid[r][c] == '#':
            direction = turn_right(direction)
        else:
            position = next_position
            visited.add(position)

    return len(visited), 1


# - parse the input map into a 2d list.
# - find the initial position/direction of the guard
# - initialize a set to track visited positions
# - while the guard is within bounds of the map:
#     - check the cell in front of the guard.
#         -if it's an obstacle, turn right.
#         - use a list of directions like ['^', '>', 'v', '<']
#         -otherwise, move one step forward.
#     - add the new position to the set of visited positions.
#        stop when the guard moves out of bounds.
#
# - output the size of the set.
#
