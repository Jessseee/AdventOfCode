# Day 17 Advent of Code
# Infinite 3d boolean matrix
import itertools as itr

import matplotlib.pyplot as plt

from aoc.helpers import *


def visualize(void, cycle, show_inactive=True):
    rows, cols, layers, slices = zip(*void.keys())
    for w in sorted(set(slices)):
        xdata, ydata, zdata = [], [], []
        for coord in void.keys():
            if coord[3] == w:
                if show_inactive or (not show_inactive and void[coord]):
                    xdata.append(coord[0])
                    ydata.append(coord[1])
                    zdata.append(coord[2])
        plt.figure(figsize=(20, 10))
        ax = plt.axes(projection="3d")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        ax.set_title(f"Cycle: {cycle}, Slice: {w}")
        ax.scatter3D(
            xdata, ydata, zdata, c=[COLORS[state] for state in void.values()] if show_inactive else [COLORS[1]]
        )
        plt.show()


def print_space(void, cycle):
    print(f"Cycle: {cycle} - ", end="")
    x1, x2, y1, y2, z1, z2, w1, w2 = get_space_edge(void)
    print(f"{x2 - x1 + 1}x{y2 - y1 + 1}x{z2 - z1 + 1}")

    row, col, layer, slices = zip(*void.keys())
    for w in sorted(set(slices)):
        print(f"w = {w}")
        for z in sorted(set(layer)):
            print(f"z = {z}")
            print("\t", end="")
            for x in sorted(set(col)):
                print(f"{x}\t", end="")
            print()
            for y in sorted(set(row)):
                print(f"{y}\t" if len(f"{y}") < 3 else f"{y} ", end="")
                for x in sorted(set(col)):
                    state = void.get((x, y, z, w))
                    print(c("☐\t", 31) if state else "☐\t", end="")
                print()
            print()


def get_space_edge(void):
    rows, cols, layers, slices = zip(*void.keys())
    x1, x2 = min(rows), max(rows)
    y1, y2 = min(cols), max(cols)
    z1, z2 = min(layers), max(layers)
    w1, w2 = min(slices), max(slices)

    return x1, x2, y1, y2, z1, z2, w1, w2


def expand_edge(void):
    new_void = void.copy()
    x1, x2, y1, y2, z1, z2, w1, w2 = get_space_edge(void)

    for x in range(x1 - 1, x2 + 2):
        for y in range(y1 - 1, y2 + 2):
            for z in range(z1 - 1, z2 + 2):
                for w in range(w1 - 1, w2 + 2):
                    coord = (x, y, z, w)
                    if coord not in void:
                        new_void[coord] = 0
    return new_void


def get_neighbours(coord):
    return [
        tuple(map(sum, zip(coord, neighbour)))
        for neighbour in itr.product([-1, 0, 1], repeat=4)
        if neighbour != (0, 0, 0, 0)
    ]


def new_states(void):
    new_void = void.copy()
    for coord, state in void.items():
        active_neighbours = 0
        for neighbour in get_neighbours(coord):
            if void.get(neighbour) == 1:
                active_neighbours += 1
        if state == 1 and active_neighbours not in [2, 3]:
            new_void[coord] = 0
        elif state == 0 and active_neighbours == 3:
            new_void[coord] = 1
    return new_void


if __name__ == "__main__":
    COLORS = [(0.3, 0.7, 1, 0.1), (1, 0.3, 0.3, 1)]
    CYCLES = 6
    VIZ_INACTIVE = False
    input = import_input().read().replace(".", "0").replace("#", "1").split("\n")

    shift = (1 - len(input)) // 2
    void = {
        (col + shift, row + shift, 0, 0): int(input[row][col])
        for row in range(len(input))
        for col in range(len(input[row]))
    }

    visualize(void, 0, VIZ_INACTIVE)
    print_space(void, 0)

    for cycle in range(CYCLES):
        void = expand_edge(void)
        void = new_states(void)
        visualize(void, cycle + 1, VIZ_INACTIVE)
        print_space(void, cycle + 1)
    print(f"Active cubes: {sum(void.values())}")
