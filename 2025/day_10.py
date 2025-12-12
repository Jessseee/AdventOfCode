# Day 10 of Advent of Code 2025
# Factory

import unittest
from collections import deque

import numpy as np
from pulp import (
    LpProblem,
    LpMinimize,
    LpVariable,
    LpInteger,
    lpSum,
    value,
    PULP_CBC_CMD,
)

from aoc.helpers import import_input, integers_from_string, timer
from aoc.library.tuples import xor


def button_to_mask(length: int):
    def mapper(button: str):
        mask = [False] * length
        for i in integers_from_string(button):
            mask[i] = True
        return tuple(mask)
    return mapper


def parser(inputs):
    machines = []
    for line in inputs.split("\n"):
        lights, *buttons, joltages = line.split(" ")
        lights = tuple(x == "#" for x in lights[1:-1])
        buttons = list(map(button_to_mask(len(lights)), buttons))
        joltages = tuple(integers_from_string(joltages))
        machines.append([lights, buttons, joltages])
    return machines


@timer()
def part1(inputs):
    total = 0
    for target, buttons, _ in inputs:
        to_visit = deque([(1, (False,) * len(target), set(range(len(buttons))))])
        explored = set()
        sequence_lengths = []
        while len(to_visit) > 0:
            presses, state, to_press = to_visit.pop()
            for i in to_press:
                next_state = xor(state, buttons[i])
                if next_state == target:
                    sequence_lengths.append(presses)
                    break
                if next_state in explored:
                    continue
                explored.add(next_state)
                to_visit.appendleft((presses + 1, next_state, to_press - {i}))
        total += min(sequence_lengths)
    return total


@timer()
def part2(inputs):
    total = 0
    for _, buttons, target in inputs:
        buttons = [list(map(int, button)) for button in buttons]
        problem = LpProblem(sense=LpMinimize)
        vars = [LpVariable(name=str(i) ,lowBound=0, cat=LpInteger) for i in range(len(buttons))]
        problem += lpSum(vars)
        for i, vector in enumerate(np.array(buttons).T):
            problem += lpSum(var * x for var, x in zip(vars, vector)) == target[i]
        problem.solve(PULP_CBC_CMD(msg=False))
        total += int(value(problem.objective))
    return total


class Tests202510(unittest.TestCase):
    inputs = parser(
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}\n"
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}\n"
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
    )

    def test_part1(self):
        expected = 7
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 33
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input(parser=parser)
    part1(inputs)
    part2(inputs)
