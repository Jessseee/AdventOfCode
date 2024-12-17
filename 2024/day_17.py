# Day 17 of Advent of Code 2024
# Chronospatial Computer

import re
import unittest

from aoc.helpers import import_input, parse_input


def parser(inputs):
    registers, program = inputs.split("\n\n")
    registers = list(map(int, re.findall(r"\d+", registers)))
    program = list(map(int, re.findall(r"\d", program)))
    return registers, program


class ThreeBitComputer:
    register_A: int
    register_B: int
    register_C: int

    def run(self, A, B, C, program):
        self.register_A = A
        self.register_B = B
        self.register_C = C
        pointer = 0
        output = []
        while pointer < len(program):
            opcode, operand = program[pointer], program[pointer + 1]
            match opcode:
                case 0:  # adv
                    self.register_A = self.divide(operand)
                case 1:  # bxl
                    self.register_B ^= operand
                case 2:  # bst
                    self.register_B = self.combo(operand) % 8
                case 3:  # jnz
                    if self.register_A != 0:
                        pointer = operand
                        continue
                case 4:  # bxc
                    self.register_B ^= self.register_C
                case 5:  # out
                    output.append(self.combo(operand) % 8)
                case 6:  # bdv
                    self.register_B = self.divide(operand)
                case 7:  # cdv
                    self.register_C = self.divide(operand)
            pointer += 2
        return output

    def divide(self, operand):
        return int(self.register_A / 2 ** self.combo(operand))

    def combo(self, operand):
        match operand:
            case 4:
                return self.register_A
            case 5:
                return self.register_B
            case 6:
                return self.register_C
            case 7:
                raise IOError("Combo operand 7 is reserved.")
            case _:
                return operand


@parse_input(parser)
def part1(inputs):
    registers, program = inputs
    computer = ThreeBitComputer()
    return ",".join(map(str, computer.run(*registers, program)))


@parse_input(parser)
def part2(inputs):
    (_, B, C), program = inputs
    computer = ThreeBitComputer()
    i = 0
    j = 1
    while True:
        output = computer.run(i, B, C, program)
        if output == program:
            return i
        if output[-j:] == program[-j:]:
            i <<= 3
            j += 1
            continue
        i += 1


class Tests202417(unittest.TestCase):
    def test_part1(self):
        inputs = "Register A: 729\nRegister B: 0\nRegister C: 0\n\nProgram: 0,1,5,4,3,0"
        expected = "4,6,3,5,6,3,5,2,1,0"
        self.assertEqual(expected, part1(inputs))

    def test_part2(self):
        inputs = "Register A: 2024\nRegister B: 0\nRegister C: 0\n\nProgram: 0,3,5,4,3,0"
        expected = 117440
        self.assertEqual(expected, part2(inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
