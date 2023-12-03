# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from functools import reduce
from operator import mul, xor

from aoc.helpers import *


class KnotHash:
    def __init__(self, inputs, salt=None, rounds=64, length=256, blocks=16):
        self.list = list(range(0, length))
        self.length = length
        self.blocks = blocks
        self.skip = 0
        self.start = 0

        if length % blocks != 0:
            raise Exception(f"{length} is not dividable into {blocks} blocks.")

        if salt:
            inputs += salt

        for _ in range(rounds):
            self.run(inputs)

    def run(self, inputs):
        for char in inputs:
            self.list[:char] = reversed(self.list[:char])
            roll = (char + self.skip) % self.length
            self.list = self.list[roll:] + self.list[:roll]
            self.start += char + self.skip
            self.skip += 1

    def sparse_hash(self):
        l = self.list.copy()
        roll = self.start % self.length
        if roll > 0:
            l = l[-roll:] + l[: self.length - roll]
        return l

    def dense_hash(self):
        dense_hash = []
        sparse_hash = self.sparse_hash()
        for i in range(self.blocks):
            num_elements = self.length // self.blocks
            offset = i * num_elements
            elements = sparse_hash[offset : offset + num_elements]
            dense_hash.append(reduce(xor, elements))
        return "".join(map(lambda i: f"{i:x}", dense_hash))


if __name__ == "__main__":
    example = False

    inputs = import_input(",", int, example=example)
    knot_hash = KnotHash(inputs, rounds=1)
    print(
        "The product of the first two numbers in the sparse Knot Hash after one round (input as numbers):",
        c(reduce(mul, knot_hash.sparse_hash()[:2]), 32),
    )

    inputs = import_input("", ord, example=example)
    salt = [17, 31, 73, 47, 23]
    knot_hash = KnotHash(inputs, salt)
    print("The final result of the Knot Hash (input as ASCII):", c(knot_hash.dense_hash(), 32))
