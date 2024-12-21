from itertools import product


# xmas = ["X", "M", "A", "S"]
xmas = ["M", "A", "S"]


def search_xmas(grilla, i, j, m, n, dir, pos):
    if pos == len(xmas):
        return 1
    if any([i < 0, i >= m, j < 0, j >= n]):
        return 0
    if pos == len(xmas) - 1:
        # busco el otro mas
        otro_mas = [
            grilla[i - (2 * dir[0])][j],
            grilla[i][j - (2 * dir[1])],
        ]
        if otro_mas not in [["M", "S"], ["S", "M"]]:
            return 0
    if grilla[i][j] == xmas[pos]:
        i += dir[0]
        j += dir[1]
        return search_xmas(grilla, i, j, m, n, dir, pos + 1)


with open("input4") as file:
    grilla = [list(line.strip()) for line in file if list(line.strip())]

    m = len(grilla)
    n = len(grilla[0])
    # dirs = list(product([1, -1, 0], repeat=2))
    # dirs.remove((0, 0))
    dirs = [(-1, -1), (1, 1)]

    count = 0

    for i in range(m):
        for j in range(n):
            for dir in dirs:
                x = search_xmas(grilla, i, j, m, n, dir, pos=0)
                if x:
                    count += 1

    print(count)
