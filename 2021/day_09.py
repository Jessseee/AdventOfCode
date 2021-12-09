# Day 9 of Advent of Code 2021
# Smoke Basin
from helpers import *
import numpy as np


def find_low_points(heightmap):
    risk_factor = 0
    low_points = set()
    x_max, y_max = heightmap.shape
    for (x, y), height in np.ndenumerate(heightmap):
        # Kindly borrowed from: https://stackoverflow.com/a/60152029/14133333
        if height == min(heightmap[max(x - 1, 0):min(x + 2, x_max), max(y - 1, 0):min(y + 2, y_max)].flatten()):
            risk_factor += height + 1
            low_points.add((x, y))
    return low_points, risk_factor


def search_basin(x, y, heightmap, basin):
    x_max, y_max = heightmap.shape
    basin.add((x, y))
    for dx in [max(x - 1, 0), min(x + 1, x_max-1)]:
        if dx != x and heightmap[dx, y] < 9 and (dx, y) not in basin:
            search_basin(dx, y, heightmap, basin)
    for dy in [max(y - 1, 0), min(y + 1, y_max-1)]:
        if dy != y and heightmap[x, dy] < 9 and (x, dy) not in basin:
            search_basin(x, dy, heightmap, basin)
    return basin


def display_basins(heightmap):
    for row in heightmap:
        for el in row:
            if el < 9:
                print(color_text(str('~'), 34), end=' ')
            else:
                print(color_text(str('0'), 33), end=' ')
        print()


def find_all_basins(heightmap, low_points):
    heightmap = heightmap.copy()
    to_visit = set()
    basins = []

    for x, y in low_points:
        basin = search_basin(x, y, heightmap, set())
        to_visit -= basin
        basins.append(len(basin))

    return basins


if __name__ == '__main__':
    heightmap = np.array([[int(x) for x in y] for y in import_input('\n', example=False)])

    display_basins(heightmap)

    low_points, risk_factor = find_low_points(heightmap)
    print(f'The total risk factor of the lowest points in the cave is: {color_text(risk_factor, 32)}')

    basins = find_all_basins(heightmap, low_points)
    top_three_basins = np.prod(sorted(basins, reverse=True)[:3])
    print(f"The product of the size of the three largest basins is: {color_text('{:,}'.format(top_three_basins), 32)}")
