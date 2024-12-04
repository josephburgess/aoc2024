
def parse_grid(data: str):
    return [list(row.strip()) for row in data.strip().splitlines()]


def count_xmas(grid: list[list[str]]) -> int:
    word = "XMAS"
    count = 0
    for row in grid:
        row_str = "".join(row)
        if word in row_str:
            count += 1
    return count


def solve(data: str):
    xmas_count = count_xmas(parse_grid(data))
    return (xmas_count, 1)
