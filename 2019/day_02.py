# Day 02 of Advent of Code 2019
# 1202 Program Alarm

import unittest
from typing import Optional
from itertools import product

from aoc.helpers import import_input


def compute_intcode(program: list[int], noun: Optional[int] = None, verb: Optional[int] = None) -> int:
    program = program.copy()
    program[1] = noun or program[1]
    program[2] = verb or program[2]
    cursor = 0
    while True:
        opcode = program[cursor]
        match opcode:
            case 1:
                lhs_addr, rhs_addr, out_addr = program[cursor+1:cursor+4]
                program[out_addr] = program[lhs_addr] + program[rhs_addr]
                cursor += 4
            case 2:
                lhs_addr, rhs_addr, out_addr = program[cursor+1:cursor+4]
                program[out_addr] = program[lhs_addr] * program[rhs_addr]
                cursor += 4
            case 99:
                return program[0]
            case _:
                raise IOError(f"Unsupported opcode '{opcode}'")


def part1(inputs):
    return compute_intcode(inputs, 12, 2)


def part2(inputs):
    for noun, verb in product(range(100), range(100)):
        if compute_intcode(inputs, noun, verb) == 19690720:
            return 100 * noun + verb


class Tests201902(unittest.TestCase):
    def test_intcode(self):
        input = [1,9,10,3,2,3,11,0,99,30,40,50]
        expected = 3500
        self.assertEqual(compute_intcode(input), expected)


if __name__ == "__main__":
    inputs = import_input(",", int)
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
