
type Machine = tuple[int, int, int, int, int, int]


def calculate_min_tokens_for_prize(a_x: int, a_y: int, b_x: int, b_y: int, prize_x: int, prize_y: int) -> int:
    min_tokens: int | None = None

    for a_presses in range(101):
        for b_presses in range(101):

            x = a_presses * a_x + b_presses * b_x
            y = a_presses * a_y + b_presses * b_y

            if x == prize_x and y == prize_y:
                tokens = a_presses * 3 + b_presses * 1
                if min_tokens is None or tokens < min_tokens:
                    min_tokens = tokens

    return min_tokens if min_tokens is not None else 0


def solve_claw_machines(machines: list[tuple[int, int, int, int, int, int]]) -> int:
    total_tokens = 0

    for a_x, a_y, b_x, b_y, prize_x, prize_y in machines:
        min_tokens = calculate_min_tokens_for_prize(a_x, a_y, b_x, b_y, prize_x, prize_y)
        if min_tokens > 0:
            total_tokens += min_tokens

    return total_tokens


def parse_input(data: str) -> list[Machine]:
    machines: list[Machine] = []

    for chunk in data.strip().split('\n\n'):
        lines = chunk.split('\n')
        a_x, a_y = map(int, lines[0].replace("Button A: X+", "").replace("Y+", "").split(", "))
        b_x, b_y = map(int, lines[1].replace("Button B: X+", "").replace("Y+", "").split(", "))
        prize_x, prize_y = map(int, lines[2].replace("Prize: X=", "").replace("Y=", "").split(", "))
        machines.append((a_x, a_y, b_x, b_y, prize_x, prize_y))

    return machines


def solve(data: str):
    machines = parse_input(data)
    total_tokens = solve_claw_machines(machines)
    return (total_tokens, 1)
