# Day 14 of Advent of Code 2024
# Restroom Redoubt

import math
import re
import unittest

from matplotlib import pyplot as plt
from scipy import ndimage

from aoc.helpers import import_input, parse_input
import numpy as np


def parser(inputs):
    return [tuple(map(int, re.findall(r"-?\d+", line))) for line in inputs.split("\n")]


@parse_input(parser)
def part1(robots, width, height):
    quadrants = [0, 0, 0, 0]
    for i, (px, py, vx, vy) in enumerate(robots):
        x, y = (px + vx * 100) % width, (py + vy * 100) % height
        if x < width//2 and y < height//2:
            quadrants[0] += 1
        elif x > width//2 and y < height//2:
            quadrants[1] += 1
        elif x > width//2 and y > height//2:
            quadrants[2] += 1
        elif x < width//2 and y > height//2:
            quadrants[3] += 1
    return math.prod(quadrants)


@parse_input(parser)
def part2(robots, width, height):
    n_robots = len(robots)
    for seconds in range(1, width * height):
        grid = np.zeros((height, width))
        for i, (px, py, vx, vy) in enumerate(robots):
            nx, ny = (px + vx * seconds) % width, (py + vy * seconds) % height
            grid[ny][nx] = 1
        input = grid > 0
        labels: np.ndarray = ndimage.label(input)[0]
        area: np.ndarray = ndimage.sum_labels(input, labels, np.arange(labels.max() + 1))
        if area[area > n_robots // 10].sum() > n_robots // 2:
            plt.imshow(area[labels])
            plt.show()
            return seconds


class Tests202414(unittest.TestCase):
    inputs = (
        "p=0,4 v=3,-3\n"
        "p=6,3 v=-1,-3\n"
        "p=10,3 v=-1,2\n"
        "p=2,0 v=2,-1\n"
        "p=0,0 v=1,3\n"
        "p=3,0 v=-2,-2\n"
        "p=7,6 v=-1,-3\n"
        "p=3,0 v=-1,-2\n"
        "p=9,3 v=2,3\n"
        "p=7,3 v=-1,2\n"
        "p=2,4 v=2,-3\n"
        "p=9,5 v=-3,-3"
    )

    def test_part1(self):
        expected = 12
        self.assertEqual(expected, part1(self.inputs, 11, 7))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs, 101, 103))
    print("part 2:", part2(inputs, 101, 103))
