
type Disk = list[int | str]


def parse_disk_map(data: str) -> Disk:
    disk: list[int | str] = []
    file_id = 0

    for i, char in enumerate(data):
        size = int(char)
        if i % 2 == 0:
            disk.extend([file_id] * size)
            file_id += 1
        else:
            disk.extend(['.'] * size)

    return disk


def compact_disk(disk: Disk) -> Disk:
    left = 0
    right = len(disk) - 1

    while left < right:
        if disk[left] == '.':
            while right > left and disk[right] == '.':
                right -= 1
            if right > left:
                disk[left], disk[right] = disk[right], disk[left]
        left += 1

    return disk


def calculate_checksum(disk: Disk) -> int:
    checksum = 0
    for i, block in enumerate(disk):
        if block != '.':
            checksum += i * int(block)
    return checksum


def solve():
    pass

# odd positions - file sizes
# even - free space sizes
# visual- input: 12345 - 1 file, 2 spaces, 3file, 4spaces, 5files
# 0..111....22222  ( and 0, 1, 2 are file IDs)
# got to isualise as continuous stream of blocks and spaces
# cells - either file blocks (rep'd as ID) or free space (.)
#
# 2333133121414131402 -> 00...111...2...333.44.5555.6666.777.888899
#
# 1. parse
# iterate through input, create a list - append blocks and space in order - ID / .
# input 2333133121414131402:
# [0, 0, '.', '.', '.', 1, 1, 1, '.', '.', '.', 2, '.', '.', '.', 3, 3, 3, '.', 4, 4, '.', 5, 5, 5, 5, '.', 6, 6, 6, 6, '.', 7, 7, 7, '.', 8, 8, 8, 8, 9, 9]
#
# thennnn compact the disk
# shift file blocks to left to fill in free space.
# WHILE loop - while there are dots to the left - sliding window
# loop through the disk to find the first free space (.).
# look to the right of that space for the nearest file block.
# move that block to the free space, filling it.
# repeat until no free spaces remain to the left of any file blocks.
#
# calculate checksum - for each block, (position) * (file ID)

# parse_disk_map(data) -> list[int|str]
#
# compact_disk(disk) -> moves file blocks left to fill gaps.
#
# calculate_checksum(disk) — Computes the checksum of the final disk state.
# checksum = 0
# for i, block in enumerate(disk):
#     if block != '.':
#         checksum += i * int(block)
# return checksum
