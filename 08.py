from itertools import permutations

antennas = {}


def substract_positions(pos1, pos2):
    return (pos1[0] - pos2[0], pos1[1] - pos2[1])


def add_positions(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])


def is_valid(pos, n, m):
    return pos[0] >= 0 and pos[0] < n and pos[1] >= 0 and pos[1] < m


with open("input8") as file:
    n = m = 0
    for i, line in enumerate(file):
        if line:
            n += 1
            m = len(line.strip())
        for j, antenna in enumerate(list(line.strip())):
            if antenna != ".":
                antennas.setdefault(antenna, set())
                antennas[antenna].add((i, j))


antinodes = set()
for antenna, positions in antennas.items():
    for pair in permutations(positions, 2):
        dist = substract_positions(pair[0], pair[1])
        antinode = add_positions(pair[0], dist)
        while is_valid(antinode, n, m):
            antinodes.add(antinode)
            antinode = add_positions(antinode, dist)
        antinodes.add(pair[0])
        antinodes.add(pair[1])

print(len(antinodes))
