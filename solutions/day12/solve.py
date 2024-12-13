from collections import deque

from custom_types import Grid, Location, Pair
from utils import parse_grid

DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def in_bounds(r: int, c: int, grid: Grid) -> bool:
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def is_valid_plot(r: int, c: int, grid: Grid, visited: set[Location], plot_type: str) -> bool:
    return (
        0 <= r < len(grid) and
        0 <= c < len(grid[0]) and
        (r, c) not in visited and
        grid[r][c] == plot_type
    )


def flood_fill(r: int, c: int, plot_type: str, visited: set[Location], grid: Grid) -> tuple[int, int]:
    if not is_valid_plot(r, c, grid, visited, plot_type):
        return 0, 0

    visited.add((r, c))

    area = 1
    perimeter = 0

    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc, grid):
            if grid[nr][nc] != plot_type:
                perimeter += 1
            elif (nr, nc) not in visited:
                sub_area, sub_perimeter = flood_fill(nr, nc, plot_type, visited, grid)
                area += sub_area
                perimeter += sub_perimeter
        else:
            perimeter += 1

    return area, perimeter


def calculate_fence_price(grid: Grid):
    visited: set[Location] = set()
    total_price = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited:
                plot_type = grid[r][c]
                area, perimeter = flood_fill(r, c, plot_type, visited, grid)
                price = area * perimeter
                total_price += price

    return total_price


def solve(data: str) -> Pair:
    price = calculate_fence_price(parse_grid(data))
    return (price, 1)


# parse into a grid
# DFS time
# area - traverse region, count plots for area - traverse in 4 directions until finding all the letters of a region
#
# perim - check all four directions of each plot (r, c) - if side is oob or touches a different plant then perim +=1
#
# price =  area × perimeter.
#
# sum region prices to get total
#
# other notes:
# visited(set) to keep track of plots already explored
#
# e.g
# start at unvisited plot (r, c).
# identify the plant type e.g. 'A'.
# explore other A's in up/down/left/right also not visted
# count plots for area of the region
# count perims while traversing
#
# keep track of the area and perimeter of each region
# use the formula price = area × perimeter for each region.
# sum the prices
