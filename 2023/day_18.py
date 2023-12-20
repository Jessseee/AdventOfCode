# Day 18 of Advent of Code 2023
# Lavaduct Lagoon

# We have successfully brought the machine parts factory into operation following the return of the lavafall,
# becoming one of the first functional factories. However, to address the substantial backlog of parts requests,
# we require an extensive supply of lava. The Elves have initiated the creation of a large lagoon nearby for this
# purpose, but doubts arise about its adequacy. Tasked with examining the dig plan, we confirm the Elves' concerns as
# the planned lagoon proves much too small. Upon investigation, it becomes evident that a mistake occurred during the
# dig plan's production – a mix-up between color and instruction parameters. With no time to fix the bug,
# the Elves request our assistance in extracting the correct instructions from the hexadecimal codes.

from aoc.helpers import *


def parse_hex_instruction(instruction):
    hex = instruction[-1]
    directions = regular_directions(True, ["3", "0", "1", "2"])
    return directions[hex[-2]], int(hex[2:-2], 16)


def parse_regular_instruction(instruction):
    directions = regular_directions(True)
    return directions[instruction[0].lower()], int(instruction[1])


def lagoon_area(instructions, parse_instruction):
    cur = (0, 0)
    trench = []
    area = 0
    length = 0
    for instruction in instructions:
        dir, dist = parse_instruction(instruction)
        length += dist
        next = add_tuples(cur, mul_tuples(dir, (dist, dist)))
        area += cur[1] * next[0] - next[1] * cur[0]
        cur = next
        trench.append(cur)
    return abs(area) // 2 + length // 2 + 1


if __name__ == "__main__":
    instructions = import_input("\n", str.split, example=False)
    print("Lagoon area:", c(lagoon_area(instructions, parse_regular_instruction), Color.GREEN))
    print("Lagoon area:", c(lagoon_area(instructions, parse_hex_instruction), Color.GREEN))
