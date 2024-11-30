# Day 17 of Advent of Code 2023
# Clumsy Crucible

# As we activate the Lava Production Facility, lava swiftly flows, and a reindeer offers us a parachute to descend
# to Gear Island. From above, we realize the island's mystery – half is empty, while the other half is a vast
# factory city. Landing near the filling lava pool, we find Elves loading crucibles on wheels to transport the lava
# throughout the city. However, steering the top-heavy crucibles is challenging, especially at high speeds,
# making long straight paths difficult. To promptly supply Desert Island with machine parts, we must strategize the
# crucible's route from the lava pool to the factory, considering minimal heat loss and avoiding long straight lines.

import bisect

import numpy as np

from aoc.helpers import *


def neighbours(current, forward, steps, max_x, max_y, min_turn, max_turn):
    neighbours = []
    if min_turn > 0 and steps < min_turn:
        x, y = add_tuples(current, forward)
        if 0 <= x < max_x and 0 <= y < max_y:
            neighbours = [((x, y), forward, steps + 1)]
    else:
        neighbours = [
            ((x, y), d, n)
            for (x, y), d, n in [
                (add_tuples(current, direction), direction, steps + 1 if direction == forward else 1)
                for direction in regular_directions()
                if direction != (-forward[0], -forward[1])
            ]
            if 0 <= x < max_x and 0 <= y < max_y and n <= max_turn
        ]
    return neighbours


def reconstruct(start, connections, current):
    shortest_path = [current]
    while current in connections:
        current = connections[current]
        if current[0] == start:
            return shortest_path
        shortest_path.insert(0, current)


def find_path(blocks, start=(0, 0), min_turn=0, max_turn=3):
    max_x, max_y = blocks.shape
    target = (max_x - 1, max_y - 1)
    current = (start, (0, 0), 0)
    connections = {}
    to_visit = [current]
    g_score = {current: 0}
    f_score = {current: blocks[current[0]]}

    while len(to_visit) > 0:
        current = to_visit.pop(0)
        if current[0] == target and current[-1] >= min_turn:
            return reconstruct_path(start, connections, current)
        for neighbour in neighbours(*current, max_x, max_y, min_turn, max_turn):
            tentative_g_score = g_score[current] + blocks[neighbour[0]]
            if tentative_g_score < g_score.get(neighbour, inf):
                connections[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + manhattan_distance(neighbour[0], target)
                if neighbour not in to_visit:
                    bisect.insort(to_visit, neighbour, key=lambda n: f_score[n])


def print_path(path, blocks):
    a = blocks.astype(str)
    for pos, dir, n in path:
        a[pos] = c({(0, 0): "X", (0, 1): "→", (1, 0): "↓", (0, -1): "←", (-1, 0): "↑"}[dir], Effect.BOLD)
    print_2d_array(a)


if __name__ == "__main__":
    blocks = np.array(import_input("\n", lambda row: [int(el) for el in list(row)]))

    path = find_path(blocks, max_turn=3)
    print("Total heat transfer (regular crucible): ", c(sum([blocks[pos] for pos, _, _ in path]), Color.GREEN))

    path = find_path(blocks, min_turn=4, max_turn=10)
    print("Total heat transfer (ultra crucible): ", c(sum([blocks[pos] for pos, _, _ in path]), Color.GREEN))
