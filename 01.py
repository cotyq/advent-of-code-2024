def day_1_1():
    list_a = []
    list_b = []
    with open("input1") as file:
        for line in file:
            list_a.append(int(line.split()[0]))
            list_b.append(int(line.split()[1]))
    list_a.sort()
    list_b.sort()

    return sum([abs(list_a[i] - list_b[i]) for i in range(len(list_a))])


def day_1_2():
    list_diff = {}

    with open("input1") as file:
        for line in file:
            [a, b] = line.split()
            list_diff.setdefault(int(a), [0, 0])
            list_diff[int(a)][0] += 1
            list_diff.setdefault(int(b), [0, 0])
            list_diff[int(b)][1] += 1

    result = sum([n * l * r for n, [l, r] in list_diff.items()])
    return result


r = day_1_1()
print(r)

r = day_1_2()
print(r)
