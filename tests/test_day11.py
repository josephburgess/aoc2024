import pytest

from solutions.day11.solve import solve, split_stone


@pytest.fixture
def example_data():
    return "125 17"


def test_split_stones():
    assert split_stone(1000) == (10, 0)


def test_example_data(example_data: str):
    assert solve(example_data) == (55312, 1)
