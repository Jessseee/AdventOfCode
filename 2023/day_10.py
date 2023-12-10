# Day 10 of Advent of Code 2023
# Pipe Maze

# We use the hang glider that happens to be lying around to ride the hot air from Desert
# Island up to the floating metal island. There does not seem to be any living creatures
# up on this island, however there are a bunch of signposts pointing to a "Hot Spring".
# On our way to these Hot Springs something metallic scurries away in our peripheral vision
# and jumps into a big pipe. We have never seen anything like this before and our tasks is
# now to find this creature in the Pipe Maze. We scan the area and make a quick sketch of
# the pipes. If we find the length and area of the loop of pipes the creature is stuck in
# we might be able to catch it.

from __future__ import annotations

from aoc.helpers import *


class Pipes:
    def __init__(self, sketch):
        self.sketch = sketch
        self.start, self.connections = self.connections_from_sketch()

    def __repr__(self):
        return self.parse_sketch(self.sketch)

    def connections_from_sketch(self):
        connections = {}
        start = None
        for row, pipes in enumerate(self.sketch.split("\n")):
            for col, pipe in enumerate(pipes):
                if pipe == ".":
                    continue
                connections[(row, col)] = self.get_connections(row, col, pipe)
                if connections[(row, col)] is None:
                    start = (row, col)
                    connections[start] = []
        for pipe, connection in connections.items():
            if start in connection:
                connections[start].append(pipe)
        return start, connections

    def get_loop(self):
        cur = self.start
        prev = None
        loop = []
        area = 0
        while True:
            connections = self.connections[cur]
            next = connections[0] if connections[0] != prev else connections[1]
            area += cur[1] * next[0] - next[1] * cur[0]  # https://en.wikipedia.org/wiki/Shoelace_formula
            prev, cur = cur, next
            loop.append(cur)
            if cur == self.start:
                return loop, abs(area) // 2

    @staticmethod
    def get_connections(row, col, pipe):
        match pipe:
            case "|":
                return (row - 1, col), (row + 1, col)
            case "-":
                return (row, col - 1), (row, col + 1)
            case "L":
                return (row - 1, col), (row, col + 1)
            case "J":
                return (row - 1, col), (row, col - 1)
            case "7":
                return (row + 1, col), (row, col - 1)
            case "F":
                return (row, col + 1), (row + 1, col)

    @staticmethod
    def parse_sketch(sketch):
        return (
            sketch.replace("|", "║")
            .replace("L", "╚")
            .replace("-", "═")
            .replace("J", "╝")
            .replace("7", "╗")
            .replace("F", "╔")
            .replace(".", ".")
            .replace("S", "◎")
        )


if __name__ == "__main__":
    pipes = Pipes(import_input().read())
    loop, area = pipes.get_loop()
    print(pipes)
    print("Length of loop:", len(loop) // 2)
    print("Tiles enclosed by loop:", area - len(loop) // 2 + 1)  # https://en.wikipedia.org/wiki/Pick%27s_theorem
