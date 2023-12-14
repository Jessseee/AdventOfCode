# Day 14 of Advent of Code 2023
# Parabolic Reflector Dish

# We reach the destination where all the mirrors converge, revealing a massive parabolic reflector dish attached
# to the side of another large mountain. The dish, comprised of numerous small mirrors, lacks proper alignment,
# scattering light aimlessly. Realizing this system powers the lava production, we discover that adjusting the
# position of rocks on a platform below the dish, connected by ropes and pulleys, allows us to control the focus.
# Additionally, the platform has a control panel enabling us to tilt it in one of four directions, providing a
# means to harness and redirect the light for fixing the lava production. However, we notice that one of the
# support beams seems to be damaged. Our task is to first test the beam by tilting the control panel and
# measuring the load on the beam.

import numpy as np

from aoc.helpers import *


def roll(rocks):
    rocks = np.rot90(rocks, -1)
    for row in range(rocks.shape[0]):
        to_shift = 0
        for col in range(rocks.shape[1]):
            match rocks[row, col]:
                case "O":
                    rocks[row, col] = "."
                    to_shift += 1
                case "#":
                    rocks[row, col - to_shift : col] = "O"
                    to_shift = 0
        rocks[row, rocks.shape[0] - to_shift :] = "O"
    return rocks


def cycle(rocks):
    for _ in range(4):
        rocks = roll(rocks)
    return rocks


def calculate_load(rocks):
    total = 0
    for (row, col), el in np.ndenumerate(rocks):
        if el == "O":
            total += len(rocks) - row
    return total


def load_after_cycles(rocks, max_cycles):
    known_states = {}
    for i in range(1, max_cycles):
        current = cycle(rocks).tobytes()
        if current in known_states:
            phase = i - known_states[current]
            if (max_cycles - i) % phase == 0:
                break
            continue
        known_states[current] = i
    return calculate_load(rocks)


if __name__ == "__main__":
    rocks = np.array(import_input("\n", list))

    load = calculate_load(np.rot90(roll(rocks), 1))
    print("Load after tilting north:", c(load, Color.GREEN))

    load = load_after_cycles(rocks, 1000000000)
    print(f"Load after 1000000000 cycles:", c(load, Color.GREEN))
