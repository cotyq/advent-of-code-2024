from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
maze = []


def add_direction(position, direction):
    return (
        position[0] + direction[0],
        position[1] + direction[1],
    )


def is_valid(position):
    return 0 <= position[0] < len(maze) and 0 <= position[1] < len(maze[0])


def is_wall(position):
    return maze[position[0]][position[1]] == "#"


def dijkstra(start):
    q = deque()
    visited = set()
    distance = {}

    q.append(start)
    distance[start] = 0

    while q:
        current = q.popleft()
        d = distance[current] + 1
        for direction in directions:
            next = add_direction(current, direction)
            if is_valid(next) and not is_wall(next) and next not in visited:
                q.append(next)
                if next not in distance:
                    distance[next] = d
                distance[next] = min(distance[next], d)
        visited.add(current)
    return distance


with open("input20") as file:
    maze = [line.strip() for line in file if line.strip()]


start = end = (0, 0)
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "S":
            start = (i, j)
        elif maze[i][j] == "E":
            end = (i, j)

distance = dijkstra(start)
total_distance = distance[end]
solutions = 0
max_cheating = 20

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if not is_wall((i, j)):
            for dx in range(-max_cheating, max_cheating + 1):
                for dy in range(-max_cheating, max_cheating + 1):
                    if 1 <= abs(dx) + abs(dy) <= max_cheating:
                        cheat_position = (i+dx, j+dy)
                        if is_valid(cheat_position) and not is_wall(cheat_position):
                            cheat_distance = distance[(i, j)] + abs(dx) + abs(dy) + total_distance - distance[cheat_position]
                            if cheat_distance <= total_distance - 100:
                               solutions += 1

print(solutions)

