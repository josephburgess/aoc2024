from custom_types import Pair
from utils import parse_grid


def solve(data: str) -> Pair:
    _ = parse_grid(data)
    return (1930, 1)


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
