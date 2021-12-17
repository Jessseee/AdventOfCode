# Day 17 of Advent of Code 2021
# Trick Shot

# Ahead of us is what appears to be a large ocean trench. Could the keys have fallen into it? We'd better send a probe
# to investigate. The probe launcher on your submarine can fire the probe with any integer velocity in the x (forward)
# and y (upward, or downward if negative) directions.

# The probe starts at position (0, 0) and moves in steps. increasing x by its x velocity and y by its y velocity.
# Due to drag the probe's x velocity changes by 1 towards the value 0 and the probe's y velocity keeps decreasing by 1.
# For the probe to successfully make it into the trench, the probe must be on some trajectory that causes it to be
# within the target area after any step. This means we will have to find an x and y velocity such that the probe is in
# the target area at any step.

# For extra flair we can shoot the probe up, so it reaches the greatest possible height before reaching the trench.
# But anyway, it might be useful to generate every possible starting velocity that makes the probe hit the target area.

from helpers import *
import numpy as np
import re


def launch_probe(x, y):
    pos = [0, 0]
    vel = [x, y]
    while pos[0] <= target[0][1] and pos[1] >= target[1][0]:
        pos = np.add(pos, vel)
        vel = np.add(vel, acc)
        vel[0] = (vel[0] > 0) * vel[0]
        if target[0][0] <= pos[0] <= target[0][1] and target[1][0] <= pos[1] <= target[1][1]:
            return True
    return False


if __name__ == '__main__':
    inputs = import_input().read()
    target = [(int(i), int(j)) for i, j in re.findall(r'(-?[0-9]+)..(-?[0-9]+)', inputs)]
    max_height = (target[1][0] + 1) * (target[1][0] // 2)
    acc = [-1, -1]
    hits = set()

    for x in range(0, 1+target[0][1]):
        for y in range(target[1][0], -target[1][0]):
            if launch_probe(x, y):
                hits.add((x, y))

    print('Maximum possible height:', max_height)
    print('Number of possible trajectories:', len(hits))

