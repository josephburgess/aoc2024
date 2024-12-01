import pytest
from solutions.day01 import parse_arrays

@pytest.fixture
def test_data():
    return """
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3
    """

class TestParseArrays:

    def test_returns_tuple_of_arrays(self, test_data: str):
        result = parse_arrays(test_data)

        assert isinstance(result, tuple)
        assert len(result) == 2
        assert isinstance(result[0], list)
        assert isinstance(result[1], list)
