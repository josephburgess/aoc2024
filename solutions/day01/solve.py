from custom_types import Solution

from .logic import calculate_distance, calculate_similarity_score, parse_arrays


def solve(data: str) -> Solution:
    left, right = parse_arrays(data)
    total_distance = calculate_distance(left, right)
    similarity_score = calculate_similarity_score(left, right)

    return total_distance, similarity_score
