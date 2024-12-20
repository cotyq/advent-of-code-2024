def day_1_1():
    list_a = []
    list_b = []
    with open("input_1_1") as file:
        for line in file:
            list_a.append(int(line.split()[0]))
            list_b.append(int(line.split()[1]))
    list_a.sort()
    list_b.sort()

    return sum([abs(list_a[i] - list_b[i]) for i in range(len(list_a))])


if __name__ == "__main__":
    r = day_1_1()
    print(r)
