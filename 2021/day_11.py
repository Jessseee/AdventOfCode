# Day 11 of Advent of Code 2021
# Dumbo Octopus

# We entered a large cavern full of rare bioluminescent dumbo octopuses! There are 100 octopuses
# arranged neatly in a 10 by 10 grid. Each octopus slowly gains energy over time and flashes
# brightly for a moment when its energy is full.

# Each octopus has an energy level. The energy level of each octopus is a value between 0 and 9
# We can model the energy levels and flashes of light in steps. During a single step, the following occurs:
# - First, the energy level of each octopus increases by 1.
# - Then, any octopus with an energy level greater than 9 flashes. Increasing the energy level of all 8 adjacent
#   octopi by 1. If this causes an octopus to have an energy level greater than 9, it also flashes.
#   This process continues as long as new octopi keep having their energy level increased beyond 9.
#   (An octopus can only flash at most once per step.)
# - Finally, any octopi that flashed during this step has its energy level reset to 0.

import numpy as np

from aoc.helpers import *


def print_octopi(octopi):
    for row in octopi:
        for octopus in row:
            if octopus == 0 or octopus > 9:
                print(c(str(octopus).zfill(2), 33), end=" ")
            else:
                print(c(str(octopus).zfill(2), 30), end=" ")
        print()
    print()


def flash(octopi, flashed):
    # Make a mask of all the flashes
    flashes = np.zeros(octopi.shape, dtype=int, order="F")
    x_max, y_max = octopi.shape
    for (x, y), energy in np.ndenumerate(octopi):
        if energy > 9 and (x, y) not in flashed:
            flashed.append((x, y))
            for nx in range(max(x - 1, 0), min(x + 2, x_max)):
                for ny in range(max(y - 1, 0), min(y + 2, y_max)):
                    flashes[nx, ny] += 1

    # Add the flash energy to all the octopi
    octopi += flashes

    # If there are still octopi left that are ready to flash: let them flash!
    if any([energy > 9 and (x, y) not in flashed for (x, y), energy in np.ndenumerate(octopi)]):
        flash(octopi, flashed)

    return octopi


if __name__ == "__main__":
    octopi = np.array([[int(x) for x in line] for line in import_input("\n")])
    print("Initial state:")
    print_octopi(octopi)

    total_flashes = 0
    simultaneous = False
    step = 0
    while not simultaneous:
        step += 1

        # Increase octopi energy levels with 1
        octopi += np.full(octopi.shape, 1)

        # Make all octopi flash recursively until all are done
        octopi = flash(octopi, [])

        # Count the number of flashes
        total_flashes += sum(sum((octopi > 10)))

        # stop execution when all octopy flash simultaneously
        if all((octopi > 10).flatten()):
            simultaneous = True

        # Reset all octopy with energy > 10 to 0
        octopi = (octopi < 10) * octopi

        print(f"After step {step}:")
        print("total flashes:", total_flashes)
        print_octopi(octopi)
