# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from helpers import *


if __name__ == '__main__':
    instructions = import_input(', ', example=False)
    direction = Vector2D(0, 1)
    position = Vector2D.zeros()
    visited = []
    visited_twice = None
    for instruction in instructions:
        rotate, distance = instruction[0], int(''.join(instruction[1:]))
        direction = direction.rotate90(rotate == 'R')
        for _ in range(distance):
            position += direction
            if position in visited: visited_twice = position.dist_manhattan()
            if not visited_twice: visited.append(position)
    final_position = position.dist_manhattan()
    print(f"The first position visited twice is {color_text(visited_twice, Color.GREEN)} blocks away.")
    print(f"The final position of the instructions is {color_text(final_position, Color.GREEN)} blocks away.")
