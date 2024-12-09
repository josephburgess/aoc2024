import pytest

from solutions.day09 import parse_disk_map, solve


@pytest.fixture
def example_data():
    return "2333133121414131402"


def test_parse_disk(example_data: str):
    assert parse_disk_map(example_data) == [0, 0, '.', '.', '.', 1, 1, 1, '.', '.', '.', 2, '.', '.', '.', 3, 3, 3, '.', 4, 4, '.', 5, 5, 5, 5, '.', 6, 6, 6, 6, '.', 7, 7, 7, '.', 8, 8, 8, 8, 9, 9]


def test_example_data(example_data: str):
    pass
