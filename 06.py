directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_next_pos(current_pos, direction):
    return (current_pos[0] + direction[0], current_pos[1] + direction[1])


def se_fue_del_mapa(map, current_pos):
    i, j = current_pos
    return i < 0 or j < 0 or i >= len(map) or j >= len(map[0])


def is_valid_pos(map, current_pos, current_obstruction):
    i, j = current_pos
    if current_pos == current_obstruction:
        return False
    if not se_fue_del_mapa(map, current_pos) and map[i][j] == "#":
        return False
    return True


def get_next_obstruction(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == ".":
                yield (i, j)


with open("input6") as file:
    map = [list(line.strip()) for line in file if line.strip()]

initial_pos = (0, 0)
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "^":
            initial_pos = (i, j)
            break


ciclos = 0

for obs in get_next_obstruction(map):
    current_pos = initial_pos
    visited = [[False] * len(map[0]) for i in map]
    visited_from = [[set() for col in map[0]] for row in map]
    current_dir = 0
    while True:
        if se_fue_del_mapa(map, current_pos):
            break
        (i, j) = current_pos
        if visited[i][j] and current_dir in visited_from[i][j]:
            ciclos += 1
            break
        visited[i][j] = True
        visited_from[i][j].add(current_dir)

        next_pos = get_next_pos(current_pos, directions[current_dir])
        while not is_valid_pos(map, next_pos, obs):
            current_dir = (current_dir + 1) % len(directions)
            next_pos = get_next_pos(current_pos, directions[current_dir])
        current_pos = next_pos

print(ciclos)
