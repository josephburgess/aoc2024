
from custom_types import Pair

type Rule = tuple[int, int]
type Update = list[int]


def parse_rules_and_updates(data: str) -> tuple[list[Rule], list[Update]]:
    lines = data.strip().splitlines()
    rules: list[Rule] = []
    updates: list[Update] = []

    for l in lines:
        if "|" in l:
            a, b = map(int, l.split("|"))
            rules.append((a, b))
        elif "," in l:
            updates.append(list(map(int, l.split(","))))

    return rules, updates


def determine_relevant_rules(rules: list[Rule], update: Update) -> list[Rule]:
    return [(page1, page2) for page1, page2 in rules if page1 in update and page2 in update]


def is_update_compliant(relevant_rules: list[Rule], update: Update) -> bool:
    return all(update.index(page1) < update.index(page2) for page1, page2 in relevant_rules)


def get_middle_page(update: Update) -> int:
    return update[len(update) // 2]


def categorise_updates(rules: list[Rule], updates: list[Update]) -> tuple[list[Update], list[Update]]:
    compliant_updates: list[Update] = []
    fixed_updates: list[Update] = []

    for update in updates:
        relevant_rules = determine_relevant_rules(rules, update)

        if is_update_compliant(relevant_rules, update):
            compliant_updates.append(update)
        else:
            fixed_updates.append(fix_non_compliant_update(relevant_rules, update))

    return compliant_updates, fixed_updates


def fix_non_compliant_update(relevant_rules: list[Rule], update: Update) -> Update:
    while True:
        fixed = False

        for page1, page2 in relevant_rules:
            i1, i2 = update.index(page1), update.index(page2)

            if i1 >= i2:
                update[i1], update[i2] = update[i2], update[i1]
                fixed = True

        if not fixed:
            break

    return update


def solve(data: str) -> Pair:
    rules, updates = parse_rules_and_updates(data)
    compliant, fixed = categorise_updates(rules, updates)
    total_compliant = sum(get_middle_page(update) for update in compliant)
    total_fixed = sum(get_middle_page(update) for update in fixed)
    return total_compliant, total_fixed
