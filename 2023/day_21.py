# Day 21 of Advent of Code 2023
# <PUZZLE TITLE>

# <PUZZLE DESCRIPTION>

from copy import deepcopy

import numpy as np
from scipy.interpolate import lagrange

from aoc.helpers import *


def steps(path, garden):
    return {
        (y + dy, x + dx)
        for y, x in path
        for dy, dx in regular_directions()
        if garden[(y + dy) % len(garden)][(x + dx) % len(garden)] != "#"
    }


if __name__ == "__main__":
    garden = np.array(import_input("\n", list, example=False))
    center = np.floor_divide(garden.shape, 2)
    width = garden.shape[0]

    xs = [center[0], center[0] + width, center[0] + 2 * width]
    ys = []
    nodes = [center]
    for i in range(1, xs[-1] + 1):
        nodes = steps(nodes, garden)
        if i in xs:
            ys.append(len(nodes))
    print(round(lagrange(xs, ys)(26501365)))
