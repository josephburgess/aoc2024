
def parse_grid(data: str):
    return [list(row.strip()) for row in data.strip().splitlines()]


def count_xmas(grid: list[list[str]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    word = "XMAS"
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (1, 1),
        (-1, 1),
        (1, -1),
    ]

    def dfs(row: int, col: int, index: int, row_step: int, col_step: int) -> bool:
        if index == len(word):
            return True
        if not (0 <= row < ROWS and 0 <= col < COLS):
            return False
        if grid[row][col] != word[index]:
            return False
        return dfs(row + row_step, col + col_step, index + 1, row_step, col_step)

    count = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == word[0]:
                for row_step, col_step in directions:
                    if dfs(row, col, 0, row_step, col_step):
                        count += 1
    return count


def count_x_mas(grid: list[list[str]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    count = 0

    def is_mas(row: int, col: int) -> bool:
        top_left = grid[row][col]
        top_right = grid[row][col + 2]
        bottom_left = grid[row + 2][col]
        bottom_right = grid[row + 2][col + 2]

        top_line = top_left + top_right
        bottom_line = bottom_left + bottom_right

        return (
            (top_line == "MS" and bottom_line == "MS") or
            (top_line == "MM" and bottom_line == "SS") or
            (top_line == "SS" and bottom_line == "MM") or
            (top_line == "SM" and bottom_line == "SM")
        )

    for row in range(ROWS - 2):
        for col in range(COLS - 2):
            if grid[row + 1][col + 1] == "A":
                if is_mas(row, col):
                    count += 1

    return count


def solve(data: str):
    xmas_count = count_xmas(parse_grid(data))
    x_mas_count = count_x_mas(parse_grid(data))
    return (xmas_count, x_mas_count)
