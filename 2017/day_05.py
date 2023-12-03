# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from aoc.helpers import *


def traverse_instructions(instructions, increment):
    cursor = 0
    steps = 0

    while 0 <= cursor < len(instructions):
        prev = cursor
        cursor += instructions[cursor]
        instructions[prev] += increment(instructions[prev])
        steps += 1
    return steps


if __name__ == "__main__":
    instructions = import_input("\n", int, example=False)

    steps = traverse_instructions(instructions.copy(), lambda x: 1)
    print(f"It took {c('{:,}'.format(steps), 32)} steps to escape the maze with simple jump increments.")

    steps = traverse_instructions(instructions.copy(), lambda x: -1 if x >= 3 else 1)
    print(f"It took {c('{:,}'.format(steps), 32)} steps to escape the maze with complex jump increments.")
