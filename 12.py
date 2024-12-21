def neighbors(map, i, j):
    n = set()
    plant = map[i][j]
    if i - 1 >= 0 and map[i-1][j] == plant:
        n.add((i-1, j))
    if j - 1 >= 0 and map[i][j-1] == plant:
        n.add((i, j-1))
    if i + 1 < len(map) and map[i+1][j] == plant:
        n.add((i+1, j))
    if j + 1 < len(map[0]) and map[i][j+1] == plant:
        n.add((i, j+1))
    return n
    
def go(map, i, j, visited, group):
    group.add((i, j))
    visited.add((i, j))
    for n in neighbors(map, i, j):
        if (i,j) not in visited:
            go(map, i, j, visited, group)


with open("input12") as file:
    map = [list(line.strip()) for line in file if line]
    n = len(map)
    m = len(map[0])
    visited = set()
    for i in range(n):
        for j in range(m):
            if (i,j) not in visited:
                group = set()
                go(map, i, j, visited, group)
                area = len(group)
                print(f"p {map[i][j]} a {area}")
    