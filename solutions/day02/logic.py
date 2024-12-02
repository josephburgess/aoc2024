
from utils import split_and_map


def parse_arrays(data: str) -> list[list[int]]:
    return split_and_map(data)


def is_safe_report(report: list[int]) -> bool:
    gaps = [abs(b - a) for a, b in zip(report, report[1:])]

    if max(gaps) > 3 or min(gaps) == 0:
        return False

    return report == sorted(report) or report == sorted(report, reverse=True)


def is_valid_with_removal(report: list[int]) -> bool:
    if is_safe_report(report):
        return True

    return any(
        is_safe_report(report[:i] + report[i + 1:]) for i in range(len(report))
    )
