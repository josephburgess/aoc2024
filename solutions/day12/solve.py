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


def flood_fill(r: int, c: int, plot_type: str, visited: set[Location], grid: Grid) -> tuple[int, int, set[Location]]:
    stack = [(r, c)]
    visited.add((r, c))
    region_cells = set([(r, c)])
    area = 0
    perimeter = 0

    while stack:
        cr, cc = stack.pop()
        area += 1

        for dr, dc in DIRECTIONS:
            nr, nc = cr + dr, cc + dc
            if in_bounds(nr, nc, grid):
                if grid[nr][nc] != plot_type:
                    perimeter += 1
                else:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc))
                        region_cells.add((nr, nc))
            else:
                perimeter += 1

    return area, perimeter, region_cells


def count_sides(region_cells: set[Location]) -> int:
    s = region_cells
    sides = 0

    def in_region(y: int, x: int):
        return (y, x) in s

    for (y, x) in region_cells:
        north = (y - 1, x)
        east = (y, x + 1)
        south = (y + 1, x)
        west = (y, x - 1)
        northeast = (y - 1, x + 1)
        southeast = (y + 1, x + 1)
        southwest = (y + 1, x - 1)
        northwest = (y - 1, x - 1)

        # outside
        if (not in_region(*north)) and (not in_region(*east)):
            sides += 1
        if (not in_region(*east)) and (not in_region(*south)):
            sides += 1
        if (not in_region(*south)) and (not in_region(*west)):
            sides += 1
        if (not in_region(*west)) and (not in_region(*north)):
            sides += 1

        # inside
        if (not in_region(*northwest)) and in_region(*north) and in_region(*west):
            sides += 1
        if (not in_region(*northeast)) and in_region(*north) and in_region(*east):
            sides += 1
        if (not in_region(*southeast)) and in_region(*south) and in_region(*east):
            sides += 1
        if (not in_region(*southwest)) and in_region(*south) and in_region(*west):
            sides += 1

    return sides


def calculate_prices(grid: Grid) -> tuple[int, int]:
    visited: set[Location] = set()
    total_part_one = 0
    total_part_two = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited:
                plot_type = grid[r][c]
                area, perimeter, region_cells = flood_fill(r, c, plot_type, visited, grid)
                region_sides = count_sides(region_cells)

                price_one = area * perimeter
                price_two = area * region_sides

                total_part_one += price_one
                total_part_two += price_two

    return total_part_one, total_part_two


def solve(data: str) -> Pair:
    grid = parse_grid(data)
    part_one_price, part_two_price = calculate_prices(grid)
    return (part_one_price, part_two_price)


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
