# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from aoc.helpers import *

if __name__ == "__main__":
    instructions = import_input(", ")
    direction = (0, 1)
    position = (0, 0)
    visited = []
    visited_twice = None
    for instruction in instructions:
        print(direction)
        rotate, distance = instruction[0], int("".join(instruction[1:]))
        direction = rotate90(direction, clockwise=(rotate == "R"))
        print(rotate, distance, direction)
        for _ in range(distance):
            position = add_tuples(position, direction)
            if position in visited:
                visited_twice = manhattan_distance(position)
            if not visited_twice:
                visited.append(position)
        print(position)
    final_position = manhattan_distance(position)
    print(f"The final position of the instructions is {c(final_position, Color.GREEN)} blocks away.")
    print(f"The first position visited twice is {c(visited_twice, Color.GREEN)} blocks away.")
