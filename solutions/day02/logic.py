
def parse_arrays(data: str) -> list[list[int]]:
    lines = data.strip().splitlines()
    result: list[list[int]] = []
    for line in lines:
        result.append([int(num) for num in line.strip().split()])
    return result

def is_safe_report(report: list[int]) -> bool:
    return (sorted(report) == report or sorted(report, reverse=True) == report)
