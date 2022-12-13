# Day 12 of Advent of Code 2022
# Hill Climbing Algorithm

# Trying to find a decent signal for our communication device we are in search of the highest point in the local area.
# We ask the device for a heightmap, and it shows us a grid of lowercase letters. Where 'a' is the lowest elevation and
# 'z' is the highest point. It also marks our current location as 'S' and the point with the best signal as 'E'. Our job
# is to find the shortest route to our destination. However, we do not want to take out our climbing gear, so we can
# only go to places with an elevation of at most one higher than our current elevation. Although a quick path up is nice
# this area might also make a great hiking trail, so we will also want to find the shortest path from any starting point
# with the lowest elevation.

from helpers import *
import numpy as np
import string
import matplotlib.pyplot as plt


def parse_height_map(heightmap):
    start = target = None
    new_heightmap = np.zeros(heightmap.shape, int)
    for (x, y), height in np.ndenumerate(heightmap):
        if height == 'S': start, height = (x, y), 'a'
        elif height == 'E': target, height = (x, y), 'z'
        new_heightmap[x, y] = string.ascii_lowercase.index(height)
    return new_heightmap, start, target,


def find_path(heightmap, start, targets, check):
    x_max, y_max = (heightmap.shape[0] - 1, heightmap.shape[1] - 1)
    linked_nodes = {}
    visited = [start]
    to_visit = [start]
    while to_visit:
        current = to_visit.pop(0)
        if current in targets:
            return linked_nodes, current
        neighbours = [(max(current[0] - 1, 0), current[1]), (min(current[0] + 1, x_max), current[1]),
                      (current[0], max(current[1] - 1, 0)), (current[0], min(current[1] + 1, y_max))]
        for neighbour in neighbours:
            if neighbour in visited or check(heightmap[current], heightmap[neighbour]):
                continue
            visited.append(neighbour)
            linked_nodes[neighbour] = current
            to_visit.append(neighbour)


def reconstruct_path(linked_nodes, destination):
    current = destination
    path_len = 0
    path = []
    while prev := linked_nodes.get(current):
        path.append(current)
        current = prev
        path_len += 1
    return path_len


def plot_map(heightmap):
    plt.matshow(heightmap)
    plt.set_cmap('hot')
    plt.colorbar()
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    heightmap = np.array(import_input('\n', list, example=False))
    heightmap, start, target = parse_height_map(heightmap)

    linked_nodes, destination = find_path(heightmap, start, [target], lambda a, b: b > a + 1)
    shortest_path = reconstruct_path(linked_nodes, destination)
    print(f"The shortest path from the start location is: {result(shortest_path)}")

    lowest_points = {i for i, height in np.ndenumerate(heightmap) if height == 0}
    linked_nodes, destination = find_path(heightmap, target, lowest_points, lambda a, b: b + 1 < a)
    shortest_path = reconstruct_path(linked_nodes, destination)
    print(f"The shortest path from any of the lowest points on the map is: {result(shortest_path)}")
