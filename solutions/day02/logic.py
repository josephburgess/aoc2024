
def parse_arrays(data: str) -> list[list[int]]:
    lines = data.strip().splitlines()
    result: list[list[int]] = []
    for line in lines:
        result.append([int(num) for num in line.strip().split()])
    return result

def is_safe_report(report: list[int]) -> bool:
    gaps = [b - a for a, b in zip(report, report[1:])]

    if max(gaps) > 3 or min(gaps) == 0:
        return False

    return report == sorted(report) or report == sorted(report, reverse=True)
