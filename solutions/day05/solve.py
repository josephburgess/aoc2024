
from custom_types import Pair

type Rule = tuple[int, int]
type Rules = list[Rule]
type Update = list[int]
type Updates = list[Update]


# Parse the Input:
def parse_rules_and_updates(data: str) -> tuple[Rules, Updates]:
    lines = data.strip().splitlines()
    rules: Rules = []
    updates: Updates = []

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
def determine_relevant_rules(rules: Rules, update: Update) -> Rules:
    relevant_rules: Rules = []
    for page1, page2 in rules:
        if page1 in update and page2 in update:
            relevant_rules.append((page1, page2))
    return relevant_rules

# Check compliance:
# - Loop through each rule and confirm that the order is maintained.


def is_update_compliant(relevant_rules: Rules, update: Update) -> bool:
    for page1, page2 in relevant_rules:
        if update.index(page1) >= update.index(page2):
            return False
    return True


def extract_middle_page(update: Update) -> int:
    return update[len(update) // 2]


def get_compliant_updates(rules: Rules, updates: Updates) -> Updates:
    compliant_updates: Updates = []
    for update in updates:
        relevant_rules = determine_relevant_rules(rules, update)
        if is_update_compliant(relevant_rules, update):
            compliant_updates.append(update)
    return compliant_updates
