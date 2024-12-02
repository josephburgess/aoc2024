
from solutions.day02.logic import parse_arrays


class TestParseLists:
    def test_single_line(self):
        data = "1 2 3 4"
        result = parse_arrays(data)
        assert result == [[1, 2, 3, 4]]

    def test_multiple_lines(self):
        data = """
        1 2 3 4
        5 6 7 8
        """
        result = parse_arrays(data)
        assert result == [[1,2,3,4],[5,6,7,8]]

