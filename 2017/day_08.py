# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
import operator
from collections import defaultdict
from dataclasses import dataclass

from pydantic import validate_arguments

from aoc.helpers import *

ops = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
    "inc": operator.add,
    "dec": operator.sub,
}


class Operator:
    def __init__(self, register, operator, value):
        self.register = register
        self.operator = ops[operator]
        self.value = int(value)


class Action(Operator):
    def __call__(self, memory):
        memory[self.register] = self.operator(memory[self.register], self.value)
        return memory


class Condition(Operator):
    def __call__(self, memory):
        return self.operator(memory[self.register], self.value)


class Instruction:
    def __init__(self, instruction, memory):
        action, condition = instruction.split("if")
        self.action = Action(*action.strip().split(" "))
        self.condition = Condition(*condition.strip().split(" "))
        self.memory = memory

    def execute(self):
        if self.condition(memory):
            self.memory = self.action(memory)


if __name__ == "__main__":
    inputs = import_input("\n", example=False)
    memory = defaultdict(lambda: 0)
    highest = 0
    for line in inputs:
        Instruction(line, memory).execute()
        highest = max(highest, max(memory.values()))
    print(f"The highest value in memory during execution was: {c(highest, 31)}.")
    print(f"The highest value in memory after execution is: {c(max(memory.values()), 31)}.")
