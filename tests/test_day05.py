from textwrap import dedent

import pytest

from solutions.day05 import parse_rules_and_updates
from solutions.day05.solve import (
    Update,
    categorise_updates,
    determine_relevant_rules,
    fix_non_compliant_update,
    is_update_compliant,
    solve,
)


@pytest.fixture
def example_data():
    return dedent("""\
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
    """)


@pytest.fixture
def real_data():
    with open("input/day05.txt", "r") as f:
        return f.read()


class TestHelpers:
    def test_parses_rules_from_input(self):
        data = dedent("""\
            47|53
            97|13
            97|61


            75,47,61,53,29
            75,29,13
        """)

        rules, updates = parse_rules_and_updates(data)
        assert rules == [(47, 53), (97, 13), (97, 61)]
        assert updates == [[75, 47, 61, 53, 29], [75, 29, 13]]

    def test_relevant_rules(self):
        rules = [(47, 53), (97, 13), (97, 61)]
        update = [75, 47, 61, 53, 29]

        assert determine_relevant_rules(rules, update) == [(47, 53)]

    def test_is_update_compliant(self):
        relevant_rules = [(47, 53)]
        update = [75, 47, 61, 53, 29]
        assert is_update_compliant(relevant_rules, update)

        relevant_rules = [(53, 47)]
        update = [75, 47, 61, 53, 29]
        assert not is_update_compliant(relevant_rules, update)

    def test_get_compliant_updates(self, example_data: str):
        rules, updates = parse_rules_and_updates(example_data)
        compliant, _ = categorise_updates(rules, updates)
        assert len(compliant) == 3

    def test_fix_non_compliant_updates(self, example_data: str):
        fixed_updates: list[Update] = []

        rules, updates = parse_rules_and_updates(example_data)
        non_compliant_updates = [updates[3], updates[4], updates[5]]
        expected = [
            [97, 75, 47, 61, 53],
            [61, 29, 13],
            [97, 75, 47, 29, 13],
        ]

        for update in non_compliant_updates:
            relevant_rules = determine_relevant_rules(rules, update)
            fixed_updates.append(fix_non_compliant_update(relevant_rules, update))

        assert fixed_updates == expected


class TestSolve:
    def test_solve_real_data(self, real_data: str):
        solution_one, _ = solve(real_data)
        assert solution_one == 4766
