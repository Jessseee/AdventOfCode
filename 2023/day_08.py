# Day 8 of Advent of Code 2023
# Haunted Wasteland

# While still riding a camel across Desert Island we suddenly sport a sandstorm approaching.
# When we turn to the Elf she suddenly disappears before our eyes. GHOSTS! One of the Camel's
# pouches has a map and instructions to find our destination. Our task is to navigate through
# the sandstorm using the given map and instructions. However, it appears the map is written
# for ghosts, not bound by the laws of spacetime. This means we will have to traverse all the
# possible paths simultaneously. We will have to figure out how many steps it will take to get
# to our destination.

import math
from itertools import cycle

from aoc.helpers import *


def steps_for_path(start_node, target, instructions):
    instructions = cycle(instructions)
    cur_node = start_node
    steps = 0
    while not target(cur_node):
        cur_node = network[cur_node][next(instructions)]
        steps += 1
    return steps


def steps_for_paths(start_nodes, target, instructions):
    steps = []
    for node in start_nodes:
        steps.append(steps_for_path(node, target, instructions))
    return math.lcm(*steps)


if __name__ == "__main__":
    _instructions, _network = import_input("\n\n")
    instructions = [instruction == "R" for instruction in _instructions]
    network = {key: value for key, *value in [re.findall(r"\w{3}", node) for node in _network.split("\n")]}

    steps = steps_for_path("AAA", lambda n: n == "ZZZ", instructions)
    print("Number of steps from 'AAA' to 'ZZZ':", c(steps, Color.GREEN))

    steps = steps_for_paths([n for n in network if n[-1] == "A"], lambda n: n[-1] == "Z", instructions)
    print("Number of steps from all '..A' to '..Z':", c(steps, Color.GREEN))
