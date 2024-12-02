from custom_types import Solution
from .logic import is_safe_report, is_valid_with_removal, parse_arrays


def solve(data: str) -> Solution:
    reports = parse_arrays(data)

    safe_reports = sum(is_safe_report(r) for r in reports)
    more_accurate_count = sum(is_valid_with_removal(r) for r in reports)

    return safe_reports, more_accurate_count
