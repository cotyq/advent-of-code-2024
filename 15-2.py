directions = {
    "<": (0, -1),
    "v": (1, 0),
    ">": (0, 1),
    "^": (-1, 0),
}

robotmap = []
instructions = ""


def add_direction(initial_pos, direction):
    return (initial_pos[0] + direction[0], initial_pos[1] + direction[1])


def set_map_position(position, character):
    robotmap[position[0]][position[1]] = character
    return robotmap


def get_map_position(position):
    return robotmap[position[0]][position[1]]


def can_move(position, direction, boxes):
    """
    Return if it's possible to move, and the list of boxes to be moved (if possible)
    """
    next_position = add_direction(position, direction)
    next_place = get_map_position(next_position)
    if next_place == "#":
        return False
    if next_place == ".":
        return True

    next_positions = [next_position]
    if direction in [directions.get("v"), directions.get("^")]:
        box_position = (
            add_direction(next_position, (0, -1))
            if next_place == "]"
            else add_direction(next_position, (0, 1))
        )
        next_positions.append(box_position)

    for n in next_positions:
        boxes.add(n)
    return all(can_move(next, direction, boxes) for next in next_positions)


with open("input15") as file:
    for line in file:
        if not line.strip():
            break
        robotmap.append(
            list(
                line.strip()
                .replace("#", "##")
                .replace("O", "[]")
                .replace(".", "..")
                .replace("@", "@.")
            )
        )

    instructions += "".join(line.strip() for line in file if line.strip())

robot = (0, 0)
for i in range(len(robotmap)):
    for j in range(len(robotmap[0])):
        if robotmap[i][j] == "@":
            robot = (i, j)
            robotmap[i][j] = "."
            break

for instruction in instructions:
    direction = directions[instruction]
    boxes = set()
    move = can_move(robot, direction, boxes)
    if move:
        robot = add_direction(robot, direction)
        box_chars = {}
        for box in boxes:
            box_chars[box] = get_map_position(box)
            set_map_position(box, ".")
        for box, box_char in box_chars.items():
            next_box = add_direction(box, direction)
            set_map_position(next_box, box_char)


count = 0
for i in range(len(robotmap)):
    for j in range(len(robotmap[0])):
        if robotmap[i][j] == "[":
            count += 100 * i + j

print(count)

