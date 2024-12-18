directions = {
  "<": (0, -1),
  "v": (1, 0),
  ">": (0, 1),
  "^": (-1, 0),
}

robotmap = []
instructions = ""


def add_direction(initial_pos, direction):
  return (
    initial_pos[0] + direction[0],
    initial_pos[1] + direction[1]
  )
  
  
def set_map_position(robotmap, position, character):
  robotmap[position[0]][position[1]] = character
  return robotmap


  
def get_map_position(robotmap, position):
  return robotmap[position[0]][position[1]]
  

with open("input15") as file:
  line = file.readline()
  while line.strip():
    robotmap.append(list(line.strip()))
    line = file.readline()
  
  instructions += "".join(line.strip() for line in file if line.strip())

  
robot = (0,0)
for i in range(len(robotmap)):
  for j in range(len(robotmap[0])):
    if robotmap[i][j] == "@":
      robot = (i, j)
      
for instruction in instructions:
  direction = directions[instruction]
  destination = add_direction(robot, direction)
  if get_map_position(robotmap, destination) == ".":
    robotmap = set_map_position(robotmap, robot, ".")
    robot = destination
    continue
  next_robot = destination
  while get_map_position(robotmap, destination) == "O":
    destination = add_direction(destination, direction)
  if get_map_position(robotmap, destination) == "#":
    continue
  robotmap = set_map_position(robotmap, destination, "O")
  robotmap = set_map_position(robotmap, next_robot, ".")
  robot = next_robot
  
count = 0
for i in range(len(robotmap)):
  for j in range(len(robotmap[0])):
    if robotmap[i][j] == "O":
      count += 100 * i + j
    
print(count)