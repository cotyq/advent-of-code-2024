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


def cheating_bfs(start, finish, original_distance, cheating_moves=1):
    q = deque()
    visited = set()
    visited.add(start)

    q.append((start, 0, visited, cheating_moves))

    solutions = 0

    while q:
        current, distance, visited, cheating_moves = q.popleft()
        if distance + 1 >= original_distance - 100:
            print("too long")
            continue
        for direction in directions:
            next = add_direction(current, direction)
            if next == finish:
                print("fin")
                if distance + 1 < original_distance - 100:
                    solutions += 1
            elif is_valid(next) and next not in visited:
                if is_wall(next) and cheating_moves:
                    next_visited = visited.copy()
                    next_visited.add(next)
                    q.append((next, distance + 1, next_visited, cheating_moves - 1))
                elif not is_wall(next):
                    next_visited = visited.copy()
                    next_visited.add(next)
                    q.append((next, distance + 1, next_visited, cheating_moves))

    return solutions


def bfs(start, finish):
    q = deque()
    visited = set()

    visited.add(start)
    q.append((start, 0))

    while q:
        current, distance = q.popleft()
        for direction in directions:
            next = add_direction(current, direction)
            if is_valid(next) and not is_wall(next) and next not in visited:
                visited.add(next)
                q.append((next, distance + 1))
                if next == finish:
                    return distance + 1


with open("input20") as file:
    maze = [line.strip() for line in file if line.strip()]

start = end = (0, 0)
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "S":
            start = (i, j)
        elif maze[i][j] == "E":
            end = (i, j)

distance = bfs(start, end)
print(distance)
solutions = cheating_bfs(start, end, distance, cheating_moves=1)
print(solutions)
