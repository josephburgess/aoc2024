
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


def determine_relevant_rules(rules: Rules, update: Update):
    relevant_rules: Rules = []
    for page1, page2 in rules:
        if page1 in update and page2 in update:
            relevant_rules.append((page1, page2))
    return relevant_rules

# Read the rules and updates.
# For Each Update:
#
# Filter the relevant rules.
# Check compliance of the update with the rules:
# Loop through each rule and confirm that the order is maintained.
# If valid, extract the middle page number.
# Sum Middle Numbers of Valid Updates.
