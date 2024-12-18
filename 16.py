maze = []
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def get_maze_position(position):
    return maze[position[0]][position[1]]


def add_direction(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])


def get_adjacent_directions(direction):
    return [
        (0 if direction[0] else 1, 0 if direction[1] else 1),
        (0 if direction[0] else -1, 0 if direction[1] else -1),
    ]


def move(position, direction):
    place = get_maze_position(position)
    if place == "E":
        return 0
    if place == "#":
        return -1

    costs = []
    print(position, direction, place)
    breakpoint()
    c = move(add_direction(position, direction), direction)
    if c >= 0:
        costs.append(c + 1)
    adjacent_directions = get_adjacent_directions(direction)
    for dir in adjacent_directions:
        next_pos = add_direction(position, dir)
        c = move(next_pos, dir)
        if c >= 0:
            costs.append(c + 1000)

    return min(costs) if costs else 0


with open("input16s") as file:
    maze = [list(line.strip()) for line in file if line.strip()]

start, end = (0, 0), (0, 0)

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "S":
            start = (i, j)
        if maze[i][j] == "E":
            end = (i, j)

cost = move(start, (0, 1))

print(cost)
