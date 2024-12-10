# find all trailheads (0) in grid[i][j]
# DFS!!
# each path only move to a cell with +1 from current
# keep track of visited cells
# track -distinct- 9 cells reached
# compute score for each trailhead (unique 9s reachable)
# dfs(x, y, height) - current position/current height
# visited - 2d array? mark cells as visited only for specific trailhead
# reachable 9s - set() for each trailhead
# check boundary / stay in grid
# once found a 9 can return (won't find another 9 if you move onwards from there)
# edge cases?
# multiple paths to the same 9 should only be counted once
# tracking of visited cells - trailID? store visited states for each trailhead separately?

from custom_types import Location, Pair

type TrailMap = list[list[int]]

DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def parse_trail_map(data: str) -> TrailMap:
    return [[int(cell) for cell in row.strip()] for row in data.strip().splitlines()]


def in_bounds(r: int, c: int, grid: TrailMap) -> bool:
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def find_trailheads(grid: TrailMap) -> list[Location]:
    return [
        (r, c)
        for r in range(len(grid))
        for c in range(len(grid[0]))
        if grid[r][c] == 0
    ]


def dfs(
    grid: TrailMap,
    r: int,
    c: int,
    visited: set[Location],
    summits: set[Location],
    path: list[Location],
    distinct_paths: set[tuple[Location, ...]]
):
    if not in_bounds(r, c, grid) or (r, c) in visited:
        return

    visited.add((r, c))
    path.append((r, c))
    current_height = grid[r][c]

    if current_height == 9:
        summits.add((r, c))
        distinct_paths.add(tuple(path))

    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc, grid) and grid[nr][nc] == current_height + 1:
            dfs(grid, nr, nc, visited, summits, path, distinct_paths)

    _ = path.pop()
    visited.remove((r, c))


def calculate_trail_scores(grid: TrailMap) -> Pair:
    total_score = 0
    total_rating = 0
    trailheads = find_trailheads(grid)

    for r, c in trailheads:
        visited: set[tuple[int, int]] = set()
        summits: set[tuple[int, int]] = set()
        path: list[tuple[int, int]] = []
        distinct_paths: set[tuple[tuple[int, int], ...]] = set()

        dfs(grid, r, c, visited, summits, path, distinct_paths)

        score = len(summits)
        rating = len(distinct_paths)
        total_score += score
        total_rating += rating

    return total_score, total_rating


def solve(data: str) -> Pair:
    return calculate_trail_scores(parse_trail_map(data))
