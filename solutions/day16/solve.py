import heapq

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve_maze(maze: list[str]) -> int | None:
    start: tuple[int, int] | None = None
    end: tuple[int, int] | None = None

    rows: int = len(maze)
    cols: int = len(maze[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    if start is None or end is None:
        raise ValueError("Maze must contain 'S' (start) and 'E' (end) tiles.")

    start_direction: int = 1

    pq: list[tuple[int, int, int, int]] = []
    heapq.heappush(pq, (0, start[0], start[1], start_direction))

    dist: dict[tuple[int, int, int], int] = {}
    dist[(start[0], start[1], start_direction)] = 0

    # dijkstra algorithm
    while pq:
        current_cost, y, x, d = heapq.heappop(pq)

        if (y, x) == end:
            return current_cost

        if dist.get((y, x, d), float('inf')) < current_cost:
            continue

        dy, dx = DIRECTIONS[d]
        ny, nx = y + dy, x + dx
        if 0 <= ny < rows and 0 <= nx < cols and maze[ny][nx] != '#':
            forward_cost: int = current_cost + 1
            if forward_cost < dist.get((ny, nx, d), float('inf')):
                dist[(ny, nx, d)] = forward_cost
                heapq.heappush(pq, (forward_cost, ny, nx, d))

        left_dir: int = (d - 1) % 4
        left_cost: int = current_cost + 1000
        if left_cost < dist.get((y, x, left_dir), float('inf')):
            dist[(y, x, left_dir)] = left_cost
            heapq.heappush(pq, (left_cost, y, x, left_dir))

        right_dir: int = (d + 1) % 4
        right_cost: int = current_cost + 1000
        if right_cost < dist.get((y, x, right_dir), float('inf')):
            dist[(y, x, right_dir)] = right_cost
            heapq.heappush(pq, (right_cost, y, x, right_dir))

    return None


def solve(data: str):
    maze = data.strip().split('\n')
    part1 = solve_maze(maze)
    return (part1, 1)

# parse the maze to find start (s) and end (e)
# initial direction is east (1)
#
# move forward (1 tile): cost = 1
# rotate left/right: cost = 1000
#
# parse list of strings
# find the start position ('s') and end position ('e').

# movement logic:
# four directions: north, east, south, west.
#  moving forward one tile (cost = 1).
#  rotating left 90deg c-clockwise (cost = 1000).
#  rotating right (90 clockwise) (cost = 1000).

# state representation:
# a state is (row, col, direction)
# use a priority queue (min-heap) to explore the lowest-cost paths first
# keep a dictionary of the best-known cost for each state to avoid reprocessing worse paths

# dijkstra's algorithm:
# start at (s, initial_direction)
# expand states by considering all valid actions (move forward, rotate left/right)
# stop when reaching the end position ('e')
