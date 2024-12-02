from custom_types import Solution
from .logic import calculate_similarity_score, parse_arrays, calculate_distance


def solve() -> Solution:
    with open("input/day01.txt", "r") as f:
        data = f.read()

    left, right = parse_arrays(data)
    total_distance = calculate_distance(left, right)
    similarity_score = calculate_similarity_score(left, right)

    return {
        "Total distance": total_distance,
        "Similarity Score": similarity_score,
    }
