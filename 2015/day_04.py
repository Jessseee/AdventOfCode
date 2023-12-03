# Day 4 of Advent of Code 2015
# The Ideal Stocking Stuffer
import hashlib

from aoc.helpers import *

if __name__ == "__main__":
    inputs = import_input(example=False).read()
    index, hash, nr_zeros = 0, "", 6
    while not hash.startswith("0" * nr_zeros):
        index += 1
        hash = hashlib.md5((inputs + str(index)).encode("utf-8")).hexdigest()
    print(f"Number to append to get {nr_zeros} zeros of starting padding: {c(index, 32)}")
    print(f"Resulting hash: {c(hash, 33)}")
