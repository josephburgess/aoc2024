import pytest

from solutions.day05 import parse_rules_and_updates


@pytest.fixture
def example_data():
    return """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


@pytest.fixture
def real_data():
    with open("input/day05.txt", "-r") as f:
        return f.read


class TestParseRules:
    def test_parses_rules_from_input(self):
        data = """
47|53
97|13
97|61


75,47,61,53,29
75,29,13
"""
        rules, updates = parse_rules_and_updates(data)
        assert rules == [(47, 53), (97, 13), (97, 61)]
        assert updates == [[75, 47, 61, 53, 29], [75, 29, 13]]
