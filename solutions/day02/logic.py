
from solutions.utils import split_and_map

def parse_arrays(data: str) -> list[list[int]]:
    return split_and_map(data)

def is_safe_report(report: list[int]) -> bool:
    gaps = [abs(b - a) for a, b in zip(report, report[1:])]

    if max(gaps) > 3 or min(gaps) == 0:
        return False

    return report == sorted(report) or report == sorted(report, reverse=True)

