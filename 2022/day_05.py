# Day 5 of Advent of Code 2022
# Supply Stacks

# Supplies for the expedition are stored stacks of cargo crates. However, to get
# the right supplies the crates need to be rearranged using a giant cargo crane.
# Our job is to simulate moving the crates into the right locations using the given
# instructions. However, there is also a fancier version of the crane that can move
# multiple crates at a time, so we might as well simulate that one too.

import re

from aoc.helpers import *


class StackMover9000:
    def __init__(self, crates, instructions):
        self.crates = self.parse_crates(crates)
        self.instructions = self.parse_instruction(instructions)

        print(f"Initializing {c(self.__class__.__name__, Color.ORANGE)} simulation...")
        print("Initial crates configuration:")
        self.print_crates()
        print()

    def move(self):
        for inst in self.instructions:
            for _ in range(inst["move"]):
                to_move = self.crates[inst["from"]].pop()
                self.crates[inst["to"]].append(to_move)

        print("Crates configuration after moving:")
        self.print_crates()
        print("Top crates after moving:", end=" ")
        self.print_top_crates()
        print()

    def print_crates(self):
        for stack in self.crates:
            print(stack)

    def print_top_crates(self):
        for stack in self.crates:
            print(c(stack[-1], Color.GREEN), end="")
        print()

    @staticmethod
    def parse_crates(crates):
        crates = crates.split("\n")[:-1]
        stacks = [[] for _ in range(1, len(crates[-1]), 4)]
        for layer in crates:
            for i in range(1, len(layer), 4):
                if layer[i] != " ":
                    stacks[i // 4].insert(0, layer[i])
        return stacks

    @staticmethod
    def parse_instruction(instructions):
        for line in instructions.split("\n"):
            instruction = re.match(r"move (\d+) from (\d+) to (\d+)", line).groups()
            inst = list(map(int, instruction))
            yield {"move": inst[0], "from": inst[1] - 1, "to": inst[2] - 1}


class StackMover9001(StackMover9000):
    def __init__(self, crates, instructions):
        super().__init__(crates, instructions)

    def move(self):
        for inst in self.instructions:
            for _ in range(inst["move"]):
                to_move = self.crates[inst["from"]][-inst["move"] :]
                self.crates[inst["to"]] = self.crates[inst["to"]] + to_move
                del self.crates[inst["from"]][-inst["move"] :]

        print("Crates configuration after moving:")
        self.print_crates()
        print("Top crates after moving:", end=" ")
        self.print_top_crates()
        print()


if __name__ == "__main__":
    crates, instructions = import_input("\n\n")
    StackMover9000(crates, instructions).move()
    StackMover9001(crates, instructions).move()
