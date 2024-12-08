
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

            if 0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols:
                antinodes.add(antinode1)

            if 0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols:
                antinodes.add(antinode2)

    return antinodes


def solve(data: str):
    grid = parse_grid(data)
    antennas = locate_antennas(grid)
    antinodes = locate_antinodes(antennas, grid)
    return (len(antinodes), 1)

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
#
