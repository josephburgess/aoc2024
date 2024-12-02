
from solutions.day02.logic import is_safe_report, parse_arrays


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

    def test_empty_input(self):
        data = ""
        result = parse_arrays(data)
        assert result == []

class TestLevelSafety:
    def test_safe_report_ascending(self):
        data = [1,2,3,4,5]
        assert is_safe_report(data)

    def test_safe_report_descending(self):
        data = [5,4,3,2,1]
        assert is_safe_report(data)
