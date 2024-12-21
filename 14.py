import re
import numpy as np


robots = []
velocities = []

with open("input14") as file:
  for line in file:
    positions = list(map(int, re.findall(r'[-+]?\d+', line)))
    robots.append(positions[:2])
    velocities.append(positions[2:])

robots = np.array(robots)
velocities = np.array(velocities)

final_pos = robots + 2 * velocities
final_pos[:, 0] = final_pos[:, 0] % 11
final_pos[:, 1] = final_pos[:, 1] % 7

print(final_pos)