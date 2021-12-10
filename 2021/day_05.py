# Day 5 of Advent of Code 2021
# Hydrothermal Venture

# We came across a field of hydrothermal vents on the ocean floor!
# These vents constantly produce large, opaque clouds, so it would be best
# to avoid them if possible. They tend to form in lines;
# the submarine helpfully produces a list of nearby lines of vents
# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2

# It is important to find the positions where multiple vents overlap,
# so we know what areas to avoid.

from helpers import *
from collections import Counter
import matplotlib.pyplot as plt


def get_points(inputs):
    points = []
    for line in inputs:
        length = max(abs(line[0][0] - line[1][0]), abs(line[0][1] - line[1][1]))
        direction = ((line[1][0] - line[0][0]) // length, (line[1][1] - line[0][1]) // length)
        for step in range(length + 1):
            point = (line[0][0] + step * direction[0], line[0][1] + step * direction[1])
            points.append(point)
    return points


def plt_vents(inputs):
    fig, ax = plt.subplots()
    ax.set_facecolor("#0f0f23")
    for line in inputs:
        ax.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]],
                linewidth=0.25, color='#00cc00')
    plt.show()


if __name__ == '__main__':
    inputs = [[tuple(int(num) for num in p.split(',')) for p in line.split(' -> ')] for line in import_input('\n')]
    points = get_points(inputs)
    overlap = Counter({k: c for k, c in Counter(points).items() if c > 1})
    print(f'There are {len(overlap)} dangerous areas where vents overlap')
    plt_vents(inputs)

