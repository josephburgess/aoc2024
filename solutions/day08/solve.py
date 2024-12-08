# Parse into grid
# find all non . chars
# for matching symbols find the coords
# if there's only one of the symbols then no antinodes can be made
# difference between coords added to opposites to find antinode
# if in bounds add to count
#                             (-1, 3), (1,-3)
# e.g. in below (1,8) (2,5) -> (0, 11), (3, 2)
def solve(data: str):
    return (14, 1)
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
# enumerate()Track row/col indices while iterating
# defaultdict(list)Store multiple positions by frequency
# itertools.combinations()Pair all antenna positions for same frequency
# set()Track unique antinode positions
# update()Merge sets of antinodes & antennas
#
# antennas = defaultdict(list)
# for r, row in enumerate(grid):
#     for c, char in enumerate(row):
#         if char != '.':
#             antennas[char].append((r, c))
#
# from itertools import combinations
#
# antinodes = set()
# rows, cols = len(grid), len(grid[0])
#
# for freq, positions in antennas.items():
#     if len(positions) < 2:
#         continue
#
#     for (r1, c1), (r2, c2) in combinations(positions, 2):
#         dr, dc = r2 - r1, c2 - c1
#         antinode1 = (r1 - dr, c1 - dc)
#         antinode2 = (r2 + dr, c2 + dc)
#
#         if 0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols:
#             antinodes.add(antinode1)
#
#         if 0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols:
#             antinodes.add(antinode2)
#
# # 4. Include antenna positions as antinodes
# for positions in antennas.values():
#     antinodes.update(positions)
#
# # 5. Count total unique positions
# result = len(antinodes)
#
