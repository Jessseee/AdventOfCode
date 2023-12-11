# Day 3 of Advent of Code 2023
# Gear Ratios

# The Elf leads us to a gondola. However, it seems to be broken, some parts are missing.
# Luckily the engineer has a schematic. Our task is to find all the part numbers of the
# engine parts, which are any numbers adjacent to a symbol on the schematic. Followed by
# finding the gear ratio, which is the product of two numbers adjacent to a '*' symbol.

from itertools import product

from numpy import prod

from aoc.helpers import *


def get_neighbours(position):
    return [
        tuple(map(sum, zip(position, neighbour))) for neighbour in product([-1, 0, 1], repeat=2) if neighbour != (0, 0)
    ]


if __name__ == "__main__":
    schematic = import_input("\n")

    # Find position/span of numbers and symbols
    numbers, symbols = [], {}
    for row, string in enumerate(schematic):
        numbers.append({})
        for match in re.finditer(r"\d+", string):
            numbers[row][match.span()] = match.group()
        for match in re.finditer(r"[^.|\w]", string):
            symbols[(row, match.start())] = match.group()

    # Find numbers neighbouring symbols
    x_max, y_max = len(schematic[0]), len(schematic)
    sum_part_numbers = sum_gear_ratios = 0
    for position, symbol in symbols.items():
        neighbours = get_neighbours(position)
        matches = {}
        for row, col in neighbours:
            for span, num in numbers[row].items():
                if col in range(*span):
                    matches[(row, span)] = int(num)
        sum_part_numbers += sum(matches.values())

        # Add gear ratio if '*' symbol has exactly two neighbouring numbers
        if symbol == "*" and len(matches) == 2:
            sum_gear_ratios += prod(list(matches.values()))

    print("Total sum of part numbers:", c(sum_part_numbers, Color.GREEN))
    print("Total sum of gear ratios:", c(sum_gear_ratios, Color.GREEN))
