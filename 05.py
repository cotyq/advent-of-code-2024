from functools import cmp_to_key

rules = set()


def comparison(a, b):
    if f"{a}|{b}" in rules:
        return -1
    if f"{b}|{a}" in rules:
        return 1
    return 0


count = 0
with open("input5") as file:
    for line in file:
        if not line.strip():
            break
        else:
            rules.add(line.strip())

    for line in file:
        update = line.strip().split(",")
        sorted_update = sorted(update, key=cmp_to_key(comparison))

        if update != sorted_update:
            count += int(sorted_update[len(sorted_update) // 2])

print(count)
