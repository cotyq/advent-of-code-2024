from collections import deque


n = 71
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
maze = []
for i in range(n):
    maze.append([1] * n)


def add_direction(position, direction):
    return (
        position[0] + direction[0],
        position[1] + direction[1],
    )


def is_valid(position):
    return (
        0 <= position[0] < n and 0 <= position[1] < n and maze[position[0]][position[1]]
    )


def print_maze():
    for line in maze:
        for x in line:
            print(f"{'.' if x else '#'}", end="")
        print()


def bfs(start, finish):
    q = deque()
    visited = set()

    visited.add(start)
    q.append((start, 0))

    while q:
        current, distance = q.popleft()
        for direction in directions:
            next = add_direction(current, direction)
            if is_valid(next) and next not in visited:
                visited.add(next)
                q.append((next, distance + 1))
                if next == finish:
                    return distance + 1
    return -1


with open("input18") as file:
    i = 0
    for line in file:
        [x, y] = line.split(",")
        maze[int(x)][int(y)] = 0
        i += 1
        if i >= 1024:
            cost = bfs((0, 0), (n - 1, n - 1))
            if cost == -1:
                print(x, y)
                break
