from custom_types import Solution
from utils import split_and_map


def parse_arrays(data: str) -> list[list[int]]:
    return split_and_map(data)


def is_safe_report(report: list[int]) -> bool:
    gaps = [abs(b - a) for a, b in zip(report, report[1:])]

    if max(gaps) > 3 or min(gaps) == 0:
        return False

    return report == sorted(report) or report == sorted(report, reverse=True)


def is_safe_with_removed_item(report: list[int]) -> bool:
    if is_safe_report(report):
        return True

    return any(
        is_safe_report(report[:i] + report[i + 1:]) for i in range(len(report))
    )


def solve(data: str) -> Solution:
    reports = parse_arrays(data)

    safe_reports = sum(is_safe_report(r) for r in reports)
    more_accurate_count = sum(is_safe_with_removed_item(r) for r in reports)

    return safe_reports, more_accurate_count
