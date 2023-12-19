# Day 16 of Advent of Code 2023
# The Floor Will Be Lava

# As we follow the reindeer through the Lava Production Facility, the focused beam of light guides us deeper into the
# cavernous surroundings. The once steel facility walls have transformed into a vast cave, with doorways, floor,
# and everything in sight composed of rocky formations. As we approach the heart of the mountain, a radiant light
# emanates from a cavern ahead, revealing that our carefully focused beam is powering a contraption on the cavern
# wall. Examining the contraption, we find a flat, two-dimensional square grid with mirrors, splitters,
# and empty spaces. The grid is positioned to utilize the beam's light, converting it into heat to melt the cavern's
# rock. To troubleshoot, the reindeer leads us to a nearby control panel, offering a collection of buttons to align
# the contraption and optimize the beam's path for maximum tile activation. Our task is to determine the
# configuration that maximizes the energy of the tiles, considering the starting position at the edge of the control
# panel.

import numpy as np

from aoc.helpers import *

down, right, up, left = regular_directions()
right_mirror = {up: left, right: down, down: right, left: up}
left_mirror = {up: right, right: up, down: left, left: down}


def calc_energy(x=0, y=0, direction=right):
    beams = [(x, y, direction)]
    energized = np.zeros_like(mirrors, dtype=bool)
    for x, y, direction in beams:
        while 0 <= x < mirrors.shape[0] and 0 <= y < mirrors.shape[1]:
            energized[y, x] = True
            match mirrors[y, x]:
                case ".":
                    pass
                case "\\":
                    direction = right_mirror[direction]
                case "/":
                    direction = left_mirror[direction]
                case "|":
                    if direction in (left, right):
                        start = (x, y, up)
                        if start in beams:
                            break
                        beams.append((x, y, up))
                        direction = down
                case "-":
                    if direction in (up, down):
                        start = (x, y, right)
                        if start in beams:
                            break
                        beams.append(start)
                        direction = left
            x, y = add_tuples((x, y), direction)
    return np.sum(energized)


def find_max_energy():
    energy = 0
    max_x, max_y = mirrors.shape
    for x in range(max_x):
        energy = max(energy, calc_energy(x, 0, down))
        energy = max(energy, calc_energy(x, max_y - 1, up))
    for y in range(max_y):
        energy = max(energy, calc_energy(0, y, down))
        energy = max(energy, calc_energy(max_x - 1, y, up))
    return energy


if __name__ == "__main__":
    mirrors = np.array(import_input("\n", list, example=False))

    print("Energy, start=(0, 0):", c(calc_energy(), Color.GREEN))
    print("Maximum energy:", c(find_max_energy(), Color.GREEN))
