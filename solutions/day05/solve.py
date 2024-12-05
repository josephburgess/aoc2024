
type Rule = tuple[int, int]
type Rules = list[Rule]
type Update = list[int]
type Updates = list[Update]


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
