
type Disk = list[int | str]
type File = tuple[int, int]  # (start, end)


def parse_disk_map(data: str) -> Disk:
    disk: list[int | str] = []
    file_id = 0
    filtered_data = ''.join(filter(str.isdigit, data))

    for i, char in enumerate(filtered_data):
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


def compact_disk_defrag(disk: Disk) -> Disk:
    files: list[File] = []
    i = 0
    while i < len(disk):
        if isinstance(disk[i], int):
            start = i
            file_id = disk[i]
            while i < len(disk) and disk[i] == file_id:
                i += 1
            end = i - 1
            files.append((start, end))
        else:
            i += 1

    files.sort(key=lambda x: disk[x[0]], reverse=True)

    def find_free_space(disk: Disk, start_idx: int, length: int) -> int:
        i = 0
        while i < start_idx:
            if disk[i] == '.':
                space_count = 0
                j = i
                while j < start_idx and j < len(disk) and disk[j] == '.' and space_count < length:
                    space_count += 1
                    j += 1
                if space_count >= length:
                    return i
                i = j
            else:
                i += 1
        return -1

    for (start, end) in files:
        file_length = end - start + 1
        file_id = disk[start]
        new_pos = find_free_space(disk, start, file_length)
        if new_pos != -1:
            for idx in range(start, end + 1):
                disk[idx] = '.'
            for idx in range(new_pos, new_pos + file_length):
                disk[idx] = file_id

    return disk


def calculate_checksum(disk: Disk) -> int:
    checksum = 0
    for i, block in enumerate(disk):
        if block != '.':
            checksum += i * int(block)
    return checksum


def solve(data: str):
    compact = compact_disk(parse_disk_map(data))
    checksum = calculate_checksum(compact)
    defrag = compact_disk_defrag(parse_disk_map(data))
    checksum_defrag = calculate_checksum(defrag)
    return (checksum, checksum_defrag)


# odd positions - file sizes
# even - free space sizes
# visual- input: 12345 - 1 file, 2 spaces, 3file, 4spaces, 5files
# 0..111....22222  ( and 0, 1, 2 are file IDs)
# got to isualise as continuous stream of blocks and spaces
# cells - either file blocks (rep'd as ID) or free space (.)
#
# 2333133121414131402 -> 00...111...2...333.44.5555.6666.777.888899
#
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
# calculate_checksum(disk) -> int  - for i/block in disk, if not space, checksum += i * block
#
#
# pt 2
# find files, store the start/indices/size and sort reverse
# find first free space that can accommodate each file
# move and mark original space as free
