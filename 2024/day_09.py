# Day 09 of Advent of Code 2024
# Disk Fragmenter

import unittest

from aoc.helpers import import_input, parse_input


def parser_part1(disk_map):
    disk_map = list(map(int, disk_map))
    disk = []
    for i, length in enumerate(disk_map):
        disk += [i // 2 if i % 2 == 0 else None for _ in range(length)]
    return disk


def find_last_occupied(disk, last_occupied):
    while disk[last_occupied] is None:
        last_occupied -= 1
    return last_occupied


@parse_input(parser_part1)
def part1(disk):
    print(disk)
    last_occupied = find_last_occupied(disk, len(disk) - 1)

    i = 0
    while i < last_occupied:
        if disk[i] is None:
            disk[i] = disk[last_occupied]
            disk[last_occupied] = None
            last_occupied = find_last_occupied(disk, last_occupied)
        i += 1

    total = 0
    for i, j in enumerate(disk[:last_occupied+1]):
        total += i * j
    return total


def parser_part2(disk_map):
    disk_map = list(map(int, disk_map))
    occupied = []
    empty = []
    position = 0
    for i, length in enumerate(disk_map):
        if i % 2 == 0:
            occupied.append((position, length))
        else:
            empty.append((position, length))
        position += length
    return occupied, empty


@parse_input(parser_part2)
def part2(inputs):
    occupied, empty = inputs
    for i, (x, occupied_size) in reversed(list(enumerate(occupied))):
        for j, (y, empty_size) in enumerate(empty):
            if empty_size >= occupied_size and y < x:
                occupied[i] = (y, occupied_size)
                empty[j] = (y+occupied_size, empty_size - occupied_size)
                break

    total = 0
    for i, (x, size) in enumerate(occupied):
        for j in range(x, x+size):
            total += i * j
    return total


class Tests202409(unittest.TestCase):
    inputs = "2333133121414131402"

    def test_part1(self):
        expected = 1928
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 2858
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
