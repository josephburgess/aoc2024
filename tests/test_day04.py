import pytest

from solutions.day04 import count_xmas, parse_grid, solve


@pytest.fixture
def real_data():
    with open("input/day04.txt", "r") as f:
        return f.read()


def test_solve(real_data: str):
    solution_one, _ = solve(real_data)
    assert solution_one == 2447


class TestParseGrid:
    def test_parse_grid(self):
        data = """
        AAAAA
        AAAAA
        AAAAA
        AAAAA
        """
        assert parse_grid(data) == [
            ["A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A"],
        ]


class TestCountXmas:

    def test_single_horizontal(self):
        example = """
            XMAS
        """
        assert count_xmas(parse_grid(example)) == 1

    def test_single_vertical(self):
        example = """
            X
            M
            A
            S
        """
        assert count_xmas(parse_grid(example)) == 1

    def test_horizontal_and_vertical(self):
        example = """
                XMAS
                MXXX
                AXXX
                SXXX
            """
        assert count_xmas(parse_grid(example)) == 2

    def test_single_horizontal_reverse(self):
        example = """
            SAMX
        """
        assert count_xmas(parse_grid(example)) == 1

    def test_single_vertical_reverse(self):
        example = """
            S
            A
            M
            X
        """
        assert count_xmas(parse_grid(example)) == 1

    def test_horizontal_and_vertical_reverse(self):
        example = """
                SAMX
                AXXX
                MXXX
                XXXX
            """
        assert count_xmas(parse_grid(example)) == 2

    def test_diagonal(self):
        example = """
                XXXX
                XMXX
                MXAX
                XXXS
            """
        assert count_xmas(parse_grid(example)) == 1

    def test_diagonal_left(self):
        example = """
                XXXX
                XXMX
                MAAX
                SXXS
            """
        assert count_xmas(parse_grid(example)) == 1

    def test_up_diagonal_left(self):
        example = """
                XXXS
                XXAX
                MMAX
                XXXS
            """
        assert count_xmas(parse_grid(example)) == 1

    def test_up_diagonal_right(self):
        example = """
                SXXX
                XAXX
                MXMX
                XXXX
            """
        assert count_xmas(parse_grid(example)) == 1

    def test_puzzle_example(self):
        example = """
            MMMSXXMASM
            MSAMXMSMSA
            AMXSXMAAMM
            MSAMASMSMX
            XMASAMXAMM
            XXAMMXXAMA
            SMSMSASXSS
            SAXAMASAAA
            MAMMMXMMMM
            MXMXAXMASX
            """

        assert count_xmas(parse_grid(example)) == 18
