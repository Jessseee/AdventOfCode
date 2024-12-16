# Day 16 of Advent of Code 2024
# Reindeer Maze

import unittest
from collections import defaultdict
from math import inf
import heapq

from aoc.helpers import import_input, parse_input


def parser(grid):
    grid = [list(row) for row in grid.split("\n")]
    start, end = None, None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "S":
                start = (x, y), (1, 0)
            if cell == "E":
                end = (x, y)
            if start and end:
                return grid, start, end


@parse_input(parser)
def part1(inputs):
    grid, start_node, target_position = inputs
    heapq.heappush(to_visit := [], (0, start_node))
    g_score = {start_node: 0}

    while len(to_visit) > 0:
        current_g_score, current_node = heapq.heappop(to_visit)
        current_position, current_direction = current_node
        if current_position == target_position:
            return current_g_score
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = neighbour = current_position[0] + dx, current_position[1] + dy
            if grid[ny][nx] == "#" or ((-dx, -dy) == current_direction):
                continue
            turn_cost = 1000 * ((dx, dy) != current_direction)
            tentative_g_score = current_g_score + 1 + turn_cost
            neighbour_node = (neighbour, (dx, dy))
            if tentative_g_score < g_score.get(neighbour_node, inf):
                g_score[neighbour_node] = tentative_g_score
                heapq.heappush(to_visit, (tentative_g_score, neighbour_node))


def find_visited(connections, current_node):
    visited = set()
    to_visit = [current_node]
    while len(to_visit) > 0:
        current = to_visit.pop()
        if current in visited:
            continue
        visited.add(current)
        to_visit.extend(connections[current])
    return {(x, y) for (x, y), _ in visited}


@parse_input(parser)
def part2(inputs):
    grid, start_node, target_position = inputs
    connections = defaultdict(list)
    heapq.heappush(to_visit := [], (0, start_node))
    g_score = {start_node: 0}

    while len(to_visit) > 0:
        current_g_score, current_node = heapq.heappop(to_visit)
        current_position, current_direction = current_node
        if current_position == target_position:
            visited = find_visited(connections, current_node)
            return len(visited)
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = neighbour_position = current_position[0] + dx, current_position[1] + dy
            if grid[ny][nx] == "#" or ((-dx, -dy) == current_direction):
                continue
            turn_cost = 1000 * ((dx, dy) != current_direction)
            tentative_g_score = g_score[(current_position, current_direction)] + 1 + turn_cost
            neighbour_node = (neighbour_position, (dx, dy))
            if tentative_g_score < g_score.get(neighbour_node, inf):
                connections[neighbour_node] = [current_node]
                g_score[neighbour_node] = tentative_g_score
                heapq.heappush(to_visit, (tentative_g_score, neighbour_node))
            if tentative_g_score == g_score.get(neighbour_node, inf):
                connections[neighbour_node].append(current_node)


class Tests202416(unittest.TestCase):
    inputs = (
        "#################\n"
        "#...#...#...#..E#\n"
        "#.#.#.#.#.#.#.#.#\n"
        "#.#.#.#...#...#.#\n"
        "#.#.#.#.###.#.#.#\n"
        "#...#.#.#.....#.#\n"
        "#.#.#.#.#.#####.#\n"
        "#.#...#.#.#.....#\n"
        "#.#.#####.#.###.#\n"
        "#.#.#.......#...#\n"
        "#.#.###.#####.###\n"
        "#.#.#...#.....#.#\n"
        "#.#.#.#####.###.#\n"
        "#.#.#.........#.#\n"
        "#.#.#.#########.#\n"
        "#S#.............#\n"
        "#################"
    )

    def test_part1(self):
        expected = 11048
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 64
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
