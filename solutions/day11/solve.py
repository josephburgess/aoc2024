# if 0, replaced by 1 stone with the number 1
# if an even number of digits, split it into two stones: one for the left half, and one for the right half (drop leading zeros 1000 would become stones 10 and 0).
# if a stone’s number has an odd number of digits, multiply it by 2024
#
# start with the initial list of stones.
# for each pass, iterate over each stone and apply the transformation rules simultaneously - don't re-do any in a pass!
# track the total number of stones after each blink(?) or just count at the end?
# stop after 25 blinks and return the total count of stones.
#
# splitting in two parts:
# convert to string? len(str(stone)) % 2 == 0
# if string is "123456", string[:len(s)//2]  string[len(s)//2:]
# split and remove leading zeros from the second part (dont think we could get leading 0s for first half..) and convert back to nums
# actually converting to int should remove the 0s anyway
#
# keep it simultaneous>
# instead of mutating list in place, build a new list for each new state
#
# how to calculate stone count:
# each blink, count the number of stones in the list.
#
# function simulate_blinks(stones, num_blinks):
#     for i from 1 to num_blinks:
#         new_stones = []
#         for stone in stones:
#             if stone == 0:
#                 new_stones.append(1)
#             else if number_of_digits(stone) is even:
#                 left_half, right_half = split_number_in_half(stone)
#                 if left_half != 0: new_stones.append(left_half)
#                 if right_half != 0: new_stones.append(right_half)
#             else:
#                 new_stones.append(stone * 2024)
#         stones = new_stones
#     return len(stones)

def parse_stones(data: str) -> list[int]:
    return [int(x) for x in data.split()]


def number_of_digits(stone: int) -> int:
    return len(str(stone))


def split_stone(stone: int) -> tuple[int, int]:
    stone_str = str(stone)
    mid = len(stone_str) // 2
    return int(stone_str[:mid]), int(stone_str[mid:])


def simulate_blinks(stones: list[int], num_blinks: int) -> int:
    for _ in range(0, num_blinks):
        new_stones: list[int] = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif (number_of_digits(stone) % 2 == 0):
                left, right = split_stone(stone)
                new_stones.append(left)
                new_stones.append(right)
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)


def solve(data: str):
    total: int = simulate_blinks(parse_stones(data), 25)
    total_two: int = simulate_blinks(parse_stones(data), 75)
    return (total, 1)
