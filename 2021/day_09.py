# Day 9 of Advent of Code 2021
# Smoke Basin

# These caves seem to be lava tubes. Parts are even still volcanically active;
# small hydrothermal vents release smoke into the caves that slowly settles like rain.

# If we can model how the smoke flows through the caves, we might be able to avoid it and be much safer.
# The submarine generates a heightmap of the floor of the nearby caves for us. And we know smoke flows to
# the lowest points on the heightmap. A low point is any locations that are lower than any of its adjacent locations.

from helpers import *
import numpy as np


def print_heightmap(heightmap):
    for row in heightmap:
        for el in row:
            if el < 9:
                print(color_text(str('~'), 34), end=' ')
            else:
                print(color_text(str('0'), 33), end=' ')
        print()


def find_low_points(heightmap):
    risk_factor = 0
    low_points = set()
    x_max, y_max = heightmap.shape
    for (x, y), height in np.ndenumerate(heightmap):
        if height == min(heightmap[max(x - 1, 0):min(x + 2, x_max), max(y - 1, 0):min(y + 2, y_max)].flatten()):
            risk_factor += height + 1
            low_points.add((x, y))
    return low_points, risk_factor


def find_basin(x, y, heightmap, basin):
    basin.add((x, y))
    x_max, y_max = heightmap.shape
    # recursively search all neighbours in a + pattern and if the height is smaller than 9 add it to the basin.
    for nx, ny in [(max(x - 1, 0), y), (min(x + 1, x_max - 1), y), (x, max(y - 1, 0)), (x, min(y + 1, y_max - 1))]:
        if heightmap[nx, ny] < 9 and (nx, ny) not in basin:
            find_basin(nx, ny, heightmap, basin)
    return basin


def find_all_basins(heightmap, low_points):
    basins = []
    for x, y in low_points:
        basin = find_basin(x, y, heightmap, set())
        basins.append(len(basin))
    return basins


if __name__ == '__main__':
    heightmap = np.array([[int(x) for x in y] for y in import_input('\n', example=False)])

    print_heightmap(heightmap)

    # First we want to find out where all the low points are in the heightmap.
    low_points, risk_factor = find_low_points(heightmap)
    print(f'The total risk factor of the lowest points in the cave is: {color_text(risk_factor, 32)}')

    # After finding. all the low points we can calculate the size of the three largest basins.
    basins = find_all_basins(heightmap, low_points)
    top_three_basins = np.prod(sorted(basins, reverse=True)[:3])
    print(f"The product of the size of the three largest basins is: {color_text('{:,}'.format(top_three_basins), 32)}")
