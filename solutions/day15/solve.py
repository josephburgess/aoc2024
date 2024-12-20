from custom_types import Grid, Location

DIRECTIONS = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}


def parse_input(input_str: str) -> tuple[Grid, str]:
    lines = [line.rstrip() for line in input_str.strip('\n').split('\n')]
    blank_line_index = 0
    for i, line in enumerate(lines):
        if not line.strip():
            blank_line_index = i
            break

    grid_lines = lines[:blank_line_index]
    moves_lines = lines[blank_line_index + 1:]

    warehouse: Grid = [list(row) for row in grid_lines]
    moves = "".join(moves_lines).replace('\n', '').strip()

    return warehouse, moves


def in_bounds(warehouse: Grid, r: int, c: int) -> bool:
    return 0 <= r < len(warehouse) and 0 <= c < len(warehouse[0])


def find_robot(warehouse: Grid) -> Location:
    for r, row in enumerate(warehouse):
        for c, val in enumerate(row):
            if val == '@':
                return r, c
    raise ValueError("robot not found!")


def push_boxes(warehouse: Grid, start_r: int, start_c: int, dr: int, dc: int) -> bool:
    boxes: list[Location] = []
    r, c = start_r, start_c
    while True:
        if in_bounds(warehouse, r, c) and warehouse[r][c] == 'O':
            boxes.append((r, c))
            r += dr
            c += dc
        else:
            break

    if not in_bounds(warehouse, r, c) or warehouse[r][c] == '#':
        return False

    if warehouse[r][c] not in ('.', '@'):
        return False

    for (br, bc) in reversed(boxes):
        warehouse[br + dr][bc + dc] = 'O'
        warehouse[br][bc] = '.'
    return True


def move_robot(warehouse: Grid, robot_pos: tuple[int, int], move: str) -> tuple[int, int]:
    r, c = robot_pos
    dr, dc = DIRECTIONS[move]
    nr, nc = r + dr, c + dc

    if not in_bounds(warehouse, nr, nc):
        return robot_pos

    target = warehouse[nr][nc]
    if target == '#':
        return robot_pos
    elif target == '.':
        warehouse[r][c], warehouse[nr][nc] = '.', '@'
        return nr, nc
    elif target == 'O':
        if push_boxes(warehouse, nr, nc, dr, dc):
            warehouse[r][c], warehouse[nr][nc] = '.', '@'
            return nr, nc
        else:
            return robot_pos
    else:
        return robot_pos


def compute_gps_sum(warehouse: Grid) -> int:
    total = 0
    for r, row in enumerate(warehouse):
        for c, val in enumerate(row):
            if val == 'O':
                total += 100 * r + c
    return total


def run_warehouse_simulation(warehouse: Grid, moves_str: str) -> int:
    robot_pos = find_robot(warehouse)

    for m in moves_str:
        robot_pos = move_robot(warehouse, robot_pos, m)

    gps_sum = compute_gps_sum(warehouse)
    return gps_sum


def solve(data: str) -> tuple[int, int]:
    grid, moves = parse_input(data)
    gps_sum = run_warehouse_simulation(grid, moves)
    return (gps_sum, 1)

# move robot (@) in grid using move list (^, v, <, >)
# push boxes (o) as needed (only if possible).
# return sum of gps coordinates for all box positions (100 * r + c for each box).
#
# parse input:
# split input into grid & move list (single string ).
# find starting robot position (@)
#
# move logic:
# for each move (^, v, <, >), calculate next cell.
# if wall (#), do nothing
# if space (.), move robot
# if box (o), try to push it and all consecutive boxes in that direction.
#     if wall or edge appears, fail push
#
# push boxes:
# find all consecutive boxes in move direction.
# if path ahead is clear (.), shift each box.
# if wall (#) cancel
#
# gps sum:
# for each box (o), calculate 100 * r + c and sum it
#
# key rules

# no movement if blocked by wall (#) or failed box push.
# gps sum is for final box positions.
#
# useful concepts
