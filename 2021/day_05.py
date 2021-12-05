# Day XX of Advent of Code 2021
# -----------------------------
from helpers import *
from collections import Counter
import matplotlib.pyplot as plt


def get_points():
    points = []
    for line in inputs:
        length = max(abs(line[0][0] - line[1][0]), abs(line[0][1] - line[1][1]))
        direction = ((line[1][0] - line[0][0]) // length, (line[1][1] - line[0][1]) // length)
        for step in range(length + 1):
            point = (line[0][0] + step * direction[0], line[0][1] + step * direction[1])
            points.append(point)
    return points


if __name__ == '__main__':
    inputs = [[tuple(int(num) for num in verts.split(',')) for verts in line.split(' -> ')] for line in import_input().read().split('\n')]
    fig, ax = plt.subplots()
    ax.set_facecolor("#0f0f23")
    for line in inputs:
        ax.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], linewidth=0.25, color='#00cc00')
    points = get_points()
    overlap = Counter({k: c for k, c in Counter(points).items() if c > 1})
    print(len(overlap))

    plt.show()
