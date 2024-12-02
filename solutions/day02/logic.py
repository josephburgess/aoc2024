
def parse_arrays(data: str) -> list[list[int]]:
    lines = data.strip().splitlines()
    result: list[list[int]] = []
    for line in lines:
        result.append([int(num) for num in line.strip().split()])
    return result

def is_safe_report(report: list[int]) -> bool:
    max_gap = max(b-a for a,b in zip(report, report[1:]))
    if max_gap > 3:
        return False
    min_gap = min(b-a for a,b in zip(report, report[1:]))
    if min_gap == 0:
        return False
    return (sorted(report) == report or sorted(report, reverse=True) == report)
