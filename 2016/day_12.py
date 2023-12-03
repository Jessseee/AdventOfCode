# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from aoc.helpers import *

registers = {"a": 0, "b": 0, "c": 0, "d": 0}


def reg_or_int(value):
    return int(value) if value.isnumeric() else registers[value]


if __name__ == "__main__":
    instructions = import_input("\n", lambda x: x.split(" "), example=False)
    cursor = 0
    step = 0
    while cursor < len(instructions):
        instruction, *values = instructions[cursor]
        match instruction:
            case "jnz":
                if reg_or_int(values[0]) != 0:
                    cursor += int(values[1]) - 1
            case "cpy":
                registers[values[1]] = reg_or_int(values[0])
            case "inc":
                registers[values[0]] += 1
            case "dec":
                registers[values[0]] -= 1
        cursor += 1
        step += 1
        if step % 10000 == 0:
            print("\rregisters:", registers, end="")
    print("\rregisters:", registers)
