
from custom_types import Pair

type Rule = tuple[int, int]
type Update = list[int]


# Parse the Input:
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


# Read the rules and updates.
# For Each Update:
# - Filter the relevant rules.
def determine_relevant_rules(rules: list[Rule], update: Update) -> list[Rule]:
    relevant_rules: list[Rule] = []
    for page1, page2 in rules:
        if page1 in update and page2 in update:
            relevant_rules.append((page1, page2))
    return relevant_rules

# Check compliance:
# - Loop through each rule and confirm that the order is maintained.


def is_update_compliant(relevant_rules: list[Rule], update: Update) -> bool:
    for page1, page2 in relevant_rules:
        if update.index(page1) >= update.index(page2):
            return False
    return True


def extract_middle_page(update: Update) -> int:
    return update[len(update) // 2]


def categorise_updates(rules: list[Rule], updates: list[Update]) -> tuple[list[Update], list[Update]]:
    compliant_updates: list[Update] = []
    non_compliant_updates: list[Update] = []
    for update in updates:
        relevant_rules = determine_relevant_rules(rules, update)
        if is_update_compliant(relevant_rules, update):
            compliant_updates.append(update)
        else:
            non_compliant_updates.append(update)
    return compliant_updates, non_compliant_updates

def fix_non_compliant_update(relevant_rules: list[Rule], update: Update) -> Update:
    while True:
        fixed = False

        for page1, page2 in relevant_rules:
            i_one, i_two = update.index(page1), update.index(page2)

            if i_one >= i_two:
                update[i_one], update[i_two] = update[i_two], update[i_one]
                fixed = True

        if not fixed:
            break

    return update


def solve(data: str) -> Pair:
    total = 0
    rules, updates = parse_rules_and_updates(data)
    compliant_updates, _ = categorise_updates(rules, updates)
    for update in compliant_updates:
        total += extract_middle_page(update)
    return (total, 1)
