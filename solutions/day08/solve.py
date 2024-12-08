
from collections import defaultdict
from itertools import combinations

from custom_types import Grid
from utils import parse_grid

type Coordinate = tuple[int, int]
type AntennaLocationMap = defaultdict[str, list[Coordinate]]


def locate_antennas(grid: Grid) -> AntennaLocationMap:
    antennas: AntennaLocationMap = defaultdict(list)
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char != ".":
                antennas[char].append((r, c))

    return antennas


def locate_antinodes(antennas: AntennaLocationMap, grid: Grid) -> set[Coordinate]:
    rows, cols = len(grid), len(grid[0])
    antinodes: set[Coordinate] = set()
    for _, locations in antennas.items():
        if len(locations) < 2:
            continue
        for (r1, c1), (r2, c2) in combinations(locations, 2):
            dr, dc = r2 - r1, c2 - c1
            antinode1 = (r1 - dr, c1 - dc)
            antinode2 = (r2 + dr, c2 + dc)

            if in_bounds(antinode1, rows, cols):
                antinodes.add(antinode1)

            if in_bounds(antinode2, rows, cols):
                antinodes.add(antinode2)

    return antinodes


def locate_antinodes_ignore_dist(antennas: AntennaLocationMap, grid: Grid) -> set[Coordinate]:
    rows, cols = len(grid), len(grid[0])
    antinodes: set[Coordinate] = set()

    def dfs(r: int, c: int, dr: int, dc: int):
        if not in_bounds((r, c), rows, cols):
            return
        antinodes.add((r, c))
        dfs(r + dr, c + dc, dr, dc)

    for _, locations in antennas.items():
        if len(locations) < 2:
            continue
        for (r1, c1), (r2, c2) in combinations(locations, 2):
            dr, dc = r2 - r1, c2 - c1

            # add the antennas themselves
            antinodes.add((r1, c1))
            antinodes.add((r2, c2))

            # recursively step outward in each dir
            dfs(r1 - dr, c1 - dc, -dr, -dc)
            dfs(r2 + dr, c2 + dc, dr, dc)

    return antinodes


def in_bounds(location: Coordinate, rows: int, cols: int) -> bool:
    r, c = location
    return 0 <= r < rows and 0 <= c < cols


def solve(data: str):
    grid = parse_grid(data)
    antennas = locate_antennas(grid)
    antinodes = locate_antinodes(antennas, grid)
    accurate_antinodes = locate_antinodes_ignore_dist(antennas, grid)
    return (len(antinodes), len(accurate_antinodes))

# Parse into grid
# find all non . chars
# for matching symbols find the coords
# if there's only one of the symbols then no antinodes can be made
# difference between coords added to opposites to find antinode
# if in bounds add to count, if not ignore
# set(antinodes)
#                             (-1, 3), (1,-3)
# e.g. in below (1,8) (2,5) -> (0, 11), (3, 2)
#             11
#   012345678901
#  0...........#
#  1........0...
#  2.....0......
#  3..#....0....
#  4....0.......
#  5......A.....
#  6............
#  7............
#  8........A...
#  9.........A..
# 10............
# 11............
#
# part 2 - another dfs? step outwards recursively until hitting oob
# add each paired antenna to the list of antinodes
