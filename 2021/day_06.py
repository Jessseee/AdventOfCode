# Day 6 of Advent of Code 2021
# Lanternfish

# A massive school of glowing lanternfish swims past. They must spawn quickly to reach such large
# numbers - maybe exponentially quickly? We should model their growth rate to be sure.
# We make the assumption that a nex lanternfish spawns each 7 days. But, this process cannot
# be synchronized between every lanternfish. luckily our submarine automatically produces a list
# of numbers for all nearby lanternfish, representing the number of days until it spawns.

# First we try our algorithm to model the spawn rate of lanternfish over 80 days.
# After we are sure our algorithm is optimised enough we can find the number
# of lanternfish after 256 days.

from helpers import *


if __name__ == '__main__':
    init_fishes = import_input(',', int)
    fishes = [0]*9
    for i in init_fishes:
        fishes[i] += 1

    for day in range(256):
        spawn = fishes.pop(0)
        fishes[6] += spawn
        fishes.append(spawn)
        if day == 79:
            print(f"After {color_text('80', 32)} days there are {color_text('{:,}'.format(sum(fishes)), 31)} angler fish!")
    print(f"After {color_text('256', 32)} days there are {color_text('{:,}'.format(sum(fishes)), 31)} angler fish!")
