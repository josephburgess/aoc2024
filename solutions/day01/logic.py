from collections import Counter


def parse_arrays(data: str) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []

    for line in data.strip().split("\n"):
        left_num, right_num = map(int, line.split())
        left.append(left_num)
        right.append(right_num)
    return (left, right)


def calculate_distance(left: list[int], right: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


def calculate_similarity_score(left: list[int], right: list[int]) -> int:
    right_counts = Counter(right)
    return sum(num * right_counts.get(num, 0) for num in left)
