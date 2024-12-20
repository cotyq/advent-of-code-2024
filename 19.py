from functools import cache

towels = []


@cache
def is_possible(pattern):
    if not pattern:
        return 1

    return sum(
        [
            is_possible(pattern[len(towel) :])
            for towel in towels
            if pattern.startswith(towel)
        ]
    )


with open("input19") as file:
    towels = file.readline().strip().split(", ")
    file.readline()
    patterns = [line.strip() for line in file if line.strip()]

count = sum(is_possible(pattern) for pattern in patterns)
print(count)
