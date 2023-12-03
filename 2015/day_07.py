# Day 7 of Advent of Code 2015
# Some Assembly Required
import operator
from collections import defaultdict

from aoc.helpers import *

operators = {
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
}


if __name__ == "__main__":
    inputs = [line.split(" -> ") for line in import_input("\n", example=False)]
    memory = defaultdict(int)
    for inst, addr in inputs:
        inst = inst.split(" ")
        if len(inst) == 1:
            inst = inst[0]
            result = int(inst) if inst.isnumeric() else memory[inst]
        elif len(inst) == 2:
            right = inst[1]
            right = right if right.isnumeric() else memory[right]
            result = ~int(right)
        else:
            left, opr, right = inst
            left = left if left.isnumeric() else memory[left]
            right = right if right.isnumeric() else memory[right]
            result = operators[opr](int(left), int(right))

        memory[addr] = result
    print(memory)
