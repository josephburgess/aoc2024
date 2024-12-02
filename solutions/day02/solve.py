from custom_types import Solution
from .logic import is_safe_report, is_valid_with_removal, parse_arrays


def solve() -> Solution:
    with open("input/day02.txt", "r") as f:
        data = f.read()

    reports = parse_arrays(data)

    count = sum(is_safe_report(r) for r in reports)
    safer_count = sum(is_valid_with_removal(r) for r in reports)

    return {
        "Safe reports": count,
        "More accurate count": safer_count,
    }
