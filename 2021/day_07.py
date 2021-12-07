# Day 7 of Advent of Code 2021
# The Treachery of Whales
from helpers import *


if __name__ == '__main__':
    init_pos = import_input(',', int)
    linear_fuel_use = min([sum([abs(pos - x) for pos in init_pos]) for x in range(max(init_pos)+1)])
    increasing_fuel_use = min([sum([abs(p - x) * (abs(p - x) + 1) // 2 for p in init_pos]) for x in range(max(init_pos) + 1)])
    print(f"It costs the crabs {color_text('{:,}'.format(linear_fuel_use), 31)} fuel to align, assuming linear fuel usage.")
    print(f"It costs the crabs {color_text('{:,}'.format(increasing_fuel_use), 31)} fuel to align, assuming increasing fuel usage.")

