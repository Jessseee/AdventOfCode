# Day 13 of Advent of Code 2023
# Point of Incidence

# With our help the hot springs team successfully locates an appropriate spring, launching us neatly
# and precisely up to the edge of Lava Island. However, we encounter a problem - no lava in sight.
# Instead, we find ourselves amidst ash and igneous rock, surrounded by gray mountains. Undeterred, we
# make our way to a cluster of mountains, discovering a valley filled with large mirrors. These mirrors,
# seemingly aligned in a consistent manner, prompt us to consider heading in that direction. As we move
# through the valley of mirrors, we find several of them have fallen from the large metal frames holding
# them in place. The mirrors, flat and shiny, have lodged into the ash at strange angles, creating a
# challenging terrain. Our task is to discern a safe walking paths from potential mirror collisions.

import numpy as np

from aoc.helpers import *


def parse_pattern(pattern):
    return np.array([[el == "#" for el in row] for row in pattern.split("\n")])


def find_mirror(pattern, with_smudge=False):
    for row in range(1, pattern.shape[0]):
        side2 = pattern[row : row + row, :]
        side1 = pattern[row - side2.shape[0] : row, :]
        if with_smudge:
            if np.sum(side1 != np.flip(side2, axis=0)) == 1:
                return row
        elif np.array_equal(side1, np.flip(side2, axis=0)):
            return row
    return 0


if __name__ == "__main__":
    patterns = import_input("\n\n", parse_pattern)

    row_total = col_total = 0
    for pattern in patterns:
        row_total += find_mirror(pattern)
        col_total += find_mirror(pattern.T)
    print("Summary of reflection lines:", c(100 * row_total + col_total, Color.GREEN))

    row_total = col_total = 0
    for pattern in patterns:
        row_total += find_mirror(pattern, True)
        col_total += find_mirror(pattern.T, True)
    print("Summary of reflection lines (with smudges):", c(100 * row_total + col_total, Color.GREEN))
