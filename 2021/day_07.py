# Day 7 of Advent of Code 2021
# The Treachery of Whales

# A giant whale has decided our submarine is its next meal, and it's much faster than we are. There's nowhere to run!
# Luckily, a swarm of crabs (each in their own tiny submarine - it's too deep for them otherwise) zooms in to rescue us!
# They seem to be preparing to blast a hole in the ocean floor; sensors indicate a massive underground cave system
# just beyond where they're aiming!

# The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for our
# submarine to get through. However, it doesn't look like they'll align before the whale catches us! Maybe we can help?

# There's one major catch - crab submarines can only move horizontally. We quickly make a list of the horizontal
# position of each crab. Crab submarines have limited fuel, so you need to find a way to make all of their
# horizontal positions match while requiring them to spend as little fuel as possible.

from aoc.helpers import *

if __name__ == "__main__":
    init_pos = import_input(",", int)

    # First we figure out what the optimal position is for the crabs to align assuming linear fuel usage.
    linear_fuel_use = min([sum([abs(pos - x) for pos in init_pos]) for x in range(max(init_pos) + 1)])
    print(f"It costs the crabs {c('{:,}'.format(linear_fuel_use), 31)} fuel to align, assuming linear fuel usage.")

    # After learning more about crab engineering we find out fuel usage is not linear but increases with n+1.
    increasing_fuel_use = min(
        [sum([abs(p - x) * (abs(p - x) + 1) // 2 for p in init_pos]) for x in range(max(init_pos) + 1)]
    )
    print(
        f"It costs the crabs {c('{:,}'.format(increasing_fuel_use), 31)} fuel to align, assuming increasing fuel usage."
    )
