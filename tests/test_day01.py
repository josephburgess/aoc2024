import pytest
from solutions.day01 import parse_arrays, calculate_distance

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

    def test_parses_correct_arrays(self, test_data: str):
        result = parse_arrays(test_data)

        left = [3, 4, 2, 1, 3, 3]
        right = [4, 3, 5, 3, 9, 3]

        assert result[0] == left
        assert result[1] == right


class TestCalculateDistance:

    def test_single_element_lists(self):
        left = [1]
        right = [1]
        result = calculate_distance(left, right)
        assert result == 0  # No distance since both elements are the same
