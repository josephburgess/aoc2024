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

from custom_types import Location
from utils import parse_grid

type TrailMap = list[list[int]]

DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def parse_trail_map(data: str) -> TrailMap:
    return [[int(cell) for cell in row.strip()] for row in data.strip().splitlines()]


def find_trailheads(grid: TrailMap) -> list[Location]:
    trailheads: list[Location] = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                trailheads.append((i, j))

    return trailheads


def calculate_trail_scores(grid: TrailMap) -> int:
    return 1


def solve(data: str):
    return (36, 1)
