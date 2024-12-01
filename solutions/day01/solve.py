from .logic import calculate_similarity_score, parse_arrays, calculate_distance


def solve():
    with open("input/day01.txt", "r") as f:
        data = f.read()

    left, right = parse_arrays(data)

    total_distance = calculate_distance(left, right)

    similarity_score = calculate_similarity_score(left, right)

    return (f"Day 1 - total distance: {total_distance}\n"
            f"Day 1 - similarity score: {similarity_score}")
