from custom_types import Solution

from collections import Counter

from utils import split_and_map

def parse_arrays(data: str) -> tuple[list[int], list[int]]:
    lines: list[list[int]] = split_and_map(data)
    left, right = map(list, zip(*lines))
    return left, right


def calculate_distance(left: list[int], right: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


def calculate_similarity_score(left: list[int], right: list[int]) -> int:
    right_counts = Counter(right)
    return sum(num * right_counts.get(num, 0) for num in left)

def solve(data: str) -> Solution:
    left, right = parse_arrays(data)
    total_distance = calculate_distance(left, right)
    similarity_score = calculate_similarity_score(left, right)

    return total_distance, similarity_score
