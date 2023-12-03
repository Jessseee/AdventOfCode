# Day 1 of Advent of Code 2021
# Sonar Sweep

# Oh, no! One of the Elves tripped and accidentally sent the sleigh keys flying into the ocean!
# Before we know it, we're inside a submarine the Elves keep ready for situations like this.
# The submarine automatically performed a sonar sweep of the sea floor.
# Each line of the input is a measurement of the sea floor depth ahead of the submarine.

from aoc.helpers import *

if __name__ == "__main__":
    inputs = [int(line.rstrip("\n")) for line in import_input("\n")]

    # First it is our job to count the number of times a depth measurement increases.
    single_increases = sum(inputs[i] < inputs[i + 1] for i in range(len(inputs) - 1))
    print(f"There are {c(single_increases, 32)} increases in the single depth measurements.")

    # For the second part we consider sums of a three-measurement sliding window
    # We count every 3 value where the sum of the next 3 values is larger
    sweep_increases = sum(sum(inputs[i : i + 3]) < sum(inputs[i + 1 : i + 4]) for i in range(len(inputs) - 4))
    print(f"There are {c(sweep_increases, 32)} increases in the sliding window depth measurements.")
