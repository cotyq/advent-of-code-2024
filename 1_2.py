def day_1_2():
    list_diff = {}

    with open("input_1_1") as file:
        for line in file:
            [a, b] = line.split()
            list_diff.setdefault(int(a), [0, 0])
            list_diff[int(a)][0] += 1
            list_diff.setdefault(int(b), [0, 0])
            list_diff[int(b)][1] += 1

    result = sum([n * l * r for n, [l, r] in list_diff.items()])
    return result


if __name__ == "__main__":
    r = day_1_2()
    print(r)
