def is_safe(line):
    levels = line.split()
    levels = [int(i) for i in levels]

    if len(levels) == 1:
        return True

    last_diff = levels[1] - levels[0]

    if not (1 <= abs(last_diff) <= 3):
        return False

    to_remove = 0

    i = 2
    while i < len(levels):
        current_diff = levels[i] - levels[i - 1]
        if current_diff * last_diff <= 0:
            if to_remove > 2:
                return False
            to_remove += 1
            current_diff = abs(levels[i] - levels[i - 2]) if i > 1 else 1
        if not (1 <= abs(current_diff) <= 3):
            return False
        last_diff = current_diff
        i += 1
    return True


def day_2_1():
    count = 0
    with open("input2") as file:
        for line in file:
            if is_safe(line):
                count += 1
    return count


if __name__ == "__main__":
    print(day_2_1())
