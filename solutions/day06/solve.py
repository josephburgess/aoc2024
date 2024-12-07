
from datetime import datetime

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


def run_patrol(position: Location, direction: str, grid: Grid) -> set[Location]:
    visited: set[Location] = set()
    start = position
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

    return visited


def run_patrol_with_obstacle(start_position: Location, start_direction: str, grid: Grid) -> int:
    loop_count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '.':
                grid[r][c] = '#'

                position = start_position
                direction = start_direction
                visited: set[tuple[Location, str]] = set()
                is_loop = False

                while True:
                    state = (position, direction)
                    if state in visited:
                        # if visited same spot in same dirction before then issa loop
                        is_loop = True
                        break
                    visited.add(state)

                    next_position = move(position, direction)
                    if not in_bounds(next_position, grid):
                        # oob == no loop
                        break

                    row, col = next_position
                    if grid[row][col] == '#':
                        direction = turn_right(direction)
                    else:
                        position = next_position

                # clean up obstacle and go again
                grid[r][c] = '.'

                if is_loop:
                    loop_count += 1

    return loop_count


def solve(data: str):

    time = datetime.now()
    start = (0, 0)
    direction = ""
    grid = parse_grid(data)
    for r, row in enumerate(grid):
        for c, location in enumerate(row):
            if location in DIRECTIONS:
                start = (r, c)
                direction = location

    visited = run_patrol(start, direction, grid)

    # NOTE: Commenting this out so that we can skip the long running computation when running
    # the root `main.py`.
    #
    # loop_count = run_patrol_with_obstacle(start, direction, grid)

    loop_count = 1

    end = datetime.now()
    total = (end - time).total_seconds()
    print(f"ran in {total:.4f} seconds")
    return len(visited), loop_count


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
# part 2: stick an obstacle on every open space and run the patrol
# store BOTH location and direction in a set - if we run into a dupe for both then we're looping
