from .logic import parse_arrays, calculate_distance

def solve():
    with open("input/day01.txt", "r") as f:
        data = f.read()

    left, right = parse_arrays(data)
    total_distance = calculate_distance(left, right)

    return f"Day 1: The total distance is {total_distance}"
