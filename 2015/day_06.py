# Day 6 of Advent of Code 2015
# Probably a Fire Hazard
import re

import matplotlib.pyplot as plt
import numpy as np

from aoc.helpers import *


def part1(inputs):
    lights = np.zeros((1000, 1000), dtype=int)
    for instruction in inputs:
        state, start, end = instruction
        if state == "off":
            lights[start[0] : end[0] + 1, start[1] : end[1] + 1] = 0
        if state == "on":
            lights[start[0] : end[0] + 1, start[1] : end[1] + 1] = 1
        if state == "toggle":
            to_toggle = lights[start[0] : end[0] + 1, start[1] : end[1] + 1].copy()
            for (x, y), v in np.ndenumerate(to_toggle):
                to_toggle[x, y] = not v
            lights[start[0] : end[0] + 1, start[1] : end[1] + 1] = to_toggle
    return lights


def part2(inputs):
    lights = np.zeros((1000, 1000), dtype=int)
    for instruction in inputs:
        state, start, end = instruction
        area = lights[start[0] : end[0] + 1, start[1] : end[1] + 1]
        states = {"off": -1, "on": 1, "toggle": 2}
        lights[start[0] : end[0] + 1, start[1] : end[1] + 1] += states[state]
        lights[start[0] : end[0] + 1, start[1] : end[1] + 1] = (area > 0) * area
    return lights


if __name__ == "__main__":
    inputs = []
    for instruction in import_input("\n", example=False):
        state, start, end = re.findall(r".*(toggle|on|off).*( [0-9]+,[0-9]+).*( [0-9]+,[0-9]+)", instruction)[0]
        inputs.append([state, tuple(map(int, start.split(","))), tuple(map(int, end.split(",")))])

    lights = part1(inputs)
    plt.imshow(lights)
    plt.show()
    print(sum(sum(lights)))

    lights = part2(inputs)
    plt.imshow(lights)
    plt.show()
    print(sum(sum(lights)))
