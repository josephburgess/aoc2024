

from solutions.day04.solve import count_xmas, parse_grid, solve


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
