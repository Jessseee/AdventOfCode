# Day 05 of Advent of Code 2024
# Print Queue

import unittest

from aoc.helpers import import_input, parse_input


def parser(inputs):
    ordering, updates = inputs.split("\n\n")
    ordering = [tuple(map(int, line.split("|"))) for line in ordering.split("\n")]
    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]
    return ordering, updates


@parse_input(parser)
def part1(inputs):
    ordering, updates = inputs
    total = 0
    for update in updates:
        rules = [rule for rule in ordering if rule[0] in update and rule[1] in update]
        if all(update.index(rule[0]) < update.index(rule[1]) for rule in rules):
            total += update[len(update)//2]
    return total


@parse_input(parser)
def part2(inputs):
    ordering, updates = inputs
    total = 0
    for update in updates:
        rules = [rule for rule in ordering if rule[0] in update and rule[1] in update]
        correct = False
        corrected = False
        while not correct:
            correct = True
            for rule in rules:
                if (i := update.index(rule[0])) > (j := update.index(rule[1])):
                    update.insert(j, update.pop(i))
                    correct = False
                    corrected = True
        if corrected:
            total += update[len(update)//2]
    return total


class Tests202405(unittest.TestCase):
    inputs = (
        "47|53\n"
        "97|13\n"
        "97|61\n"
        "97|47\n"
        "75|29\n"
        "61|13\n"
        "75|53\n"
        "29|13\n"
        "97|29\n"
        "53|29\n"
        "61|53\n"
        "97|53\n"
        "61|29\n"
        "47|13\n"
        "75|47\n"
        "97|75\n"
        "47|61\n"
        "75|61\n"
        "47|29\n"
        "75|13\n"
        "53|13\n\n"
        "75,47,61,53,29\n"
        "97,61,53,29,13\n"
        "75,29,13\n"
        "75,97,47,61,53\n"
        "61,13,29\n"
        "97,13,75,29,47"
    )

    def test_part1(self):
        expected = 143
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 123
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
