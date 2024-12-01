
def parse_arrays(data: str) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []

    for line in data.strip().split("\n"):
        parts = line.split()
        left.append(int(parts[0]))
        right.append(int(parts[1]))
    return (left, right)


def calculate_distance(left: list[int], right: list[int]) -> int:
    return abs(left[0] - right[0])
