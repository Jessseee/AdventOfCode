# Day 13 of Advent of Code 2021
# Transparent Origami

# We reached another volcanically active part of the cave. It would be nice if we could do some kind of thermal imaging,
# so we could tell ahead of time which caves are too hot to safely enter. Fortunately, the submarine seems to be
# equipped with a thermal camera! When you activate it, you are greeted with:
# --- Congratulations on your purchase! To activate this infrared thermal imaging ---
# ---      camera system, please enter the code found on page 1 of the manual.    ---

# Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual;
# as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper
# is marked with random dots and includes instructions on how to fold it up.

# Our input contains first a list of coordinates of the dots on the transparent paper and after that
# a list of fold instructions. Each instruction indicates a line on the transparent paper and wants us to
# fold the paper up (for horizontal y=... lines) or to the left (for vertical x=... lines).

# Our job is to fold up the paper correctly and find the 8 character code to activate the thermal camera.

import matplotlib.pyplot as plt
import numpy as np

from aoc.helpers import *


def fold(side1, side2, half):
    # If either side of the fold is larger than the other add the smaller side to the larger side at the fold
    diff = (side1.shape[0] - side2.shape[0], side1.shape[1] - side2.shape[1])
    if index < half:
        side2[diff[0] : side1.shape[0] + diff[0], diff[1] : side1.shape[1] + diff[1]] += side1
        return side2
    elif index > half:
        side1[diff[0] : side2.shape[0] + diff[0], diff[1] : side2.shape[1] + diff[1]] += side2
        return side1
    # If both sides are equal simply add them together
    else:
        return side1 + side2


if __name__ == "__main__":
    dots, instructions = import_input("\n\n")
    dots = np.array([tuple(map(int, line.split(","))) for line in dots.split("\n")])
    instructions = [(d[-1], int(i)) for d, i in [line.split("=") for line in instructions.split("\n")]]
    paper_shape = (max(dots[:, 1]) + 1, max(dots[:, 0]) + 1)
    paper = np.zeros(paper_shape, bool)
    for dot in dots:
        paper[dot[1], dot[0]] = 1

    for direction, index in instructions:
        if direction == "y":
            top = paper[:index, :]
            bottom = np.flipud(paper[index + 1 :, :])
            paper = fold(top, bottom, paper.shape[1] / 2)

        if direction == "x":
            left = paper[:, :index]
            right = np.fliplr(paper[:, index + 1 :])
            paper = fold(left, right, paper.shape[0] / 2)

    plt.imshow(paper)
    plt.show()
