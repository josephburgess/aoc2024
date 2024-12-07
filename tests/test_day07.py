from textwrap import dedent

import pytest

from solutions.day07.solve import parse_input, solve


@pytest.fixture
def example_data():
    return dedent(
        """
        190: 10 19
        3267: 81 40 27
        83: 17 5
        156: 15 6
        7290: 6 8 6 15
        161011: 16 10 13
        192: 17 8 14
        21037: 9 7 18 13
        292: 11 6 16 20
        """
    )


def test_example_data(example_data: str):
    assert solve(example_data) == (3749, 1)


class TestHelpers:
    def test_parse_data(self):

        data = dedent(
            """
        190: 10 19
        3267: 81 40 27
        """
        )
        assert parse_input(data) == [(190, [10, 19]), (3267, [81, 40, 27])]
