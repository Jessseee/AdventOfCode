# Day 15 of Advent of Code 2024
# Warehouse Woes

import unittest

from aoc.helpers import import_input, parse_input


def parser_part1(inputs):
    grid, instructions = inputs.split("\n\n")
    grid = [list(row) for row in grid.split("\n")]
    instructions = instructions.replace("\n", "")
    robot = None
    boxes = set()
    walls = set()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            match cell:
                case "@":
                    robot = (x, y)
                case "O":
                    boxes.add((x, y))
                case "#":
                    walls.add((x, y))
    return grid, instructions, robot, boxes, walls


@parse_input(parser_part1)
def part1(inputs):
    grid, instructions, robot, boxes, walls = inputs
    directions = {"v": (0, 1), ">": (1, 0), "^": (0, -1), "<": (-1, 0)}
    for instruction in instructions:
        dx, dy = directions[instruction]
        nx, ny = robot[0] + dx, robot[1] + dy
        if (nx, ny) in walls:
            continue
        if (nx, ny) in boxes:
            bx, by = nx, ny
            to_move = set()
            while (bx, by) in boxes:
                to_move.add((bx, by))
                bx, by = bx + dx, by + dy
                if (bx, by) in walls:
                    to_move.clear()
                    break
            if not to_move:
                continue
            boxes -= to_move
            for bx, by in to_move:
                boxes.add((bx + dx, by + dy))
        robot = (nx, ny)
    return sum(100 * y + x for x, y in boxes)


def parser_part2(inputs):
    grid, instructions = inputs.split("\n\n")
    grid = [list(row) for row in grid.split("\n")]
    instructions = instructions.replace("\n", "")
    robot = None
    boxes = set()
    walls = set()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            match cell:
                case "@":
                    robot = (x, y)
                case "O":
                    boxes.add(((x, y), (x+0.5, y)))
                case "#":
                    walls.add((x, y))
                    walls.add((x+0.5, y))
    return grid, instructions, robot, boxes, walls


@parse_input(parser_part2)
def part2(inputs):
    grid, instructions, robot, boxes, walls = inputs
    directions = {"v": (0, 1), ">": (0.5, 0), "^": (0, -1), "<": (-0.5, 0)}
    for instruction in instructions:
        dx, dy = directions[instruction]
        nx, ny = robot[0] + dx, robot[1] + dy
        if (nx, ny) in walls:
            continue
        to_move = set()
        to_check = {(nx, ny)}
        hit_wall = False
        while len(to_check) > 0 and not hit_wall:
            x, y = to_check.pop()
            for box in boxes:
                if (x, y) in walls:
                    hit_wall = True
                    break
                if (x, y) not in box or box in to_move:
                    continue
                to_move.add(box)
                x, y = x + dx, y + dy
                to_check.add((x, y))
                if y == 0:
                    to_check.add((x + dx, y))
                else:
                    (bx1, by1), (bx2, by2) = box
                    to_check.add((bx1 + dx, by1 + dy))
                    to_check.add((bx2 + dx, by2 + dy))
        if to_move and not hit_wall:
            boxes -= to_move
            for (x1, y1), (x2, y2) in to_move:
                boxes.add(((x1 + dx, y1 + dy), (x2 + dx, y2 + dy)))
        if not hit_wall:
            robot = (nx, ny)
    return int(sum(100 * y + x * 2 for (x, y), _ in boxes))


class Tests202415(unittest.TestCase):
    inputs = (
        "##########\n"
        "#..O..O.O#\n"
        "#......O.#\n"
        "#.OO..O.O#\n"
        "#..O@..O.#\n"
        "#O#..O...#\n"
        "#O..O..O.#\n"
        "#.OO.O.OO#\n"
        "#....O...#\n"
        "##########\n"
        "\n"
        "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv\n"
        "<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v"
        "^^<^^vv<<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^^><^><>>><>^^<<^^v>>><^<v"
        ">^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v"
        "^><<<^>>^v<v^v<v^>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^<><^^>^^^<><vvvvv"
        "^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv"
        "<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"
    )

    def test_part1(self):
        expected = 10092
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 9021
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
