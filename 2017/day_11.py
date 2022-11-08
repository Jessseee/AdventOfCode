# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from helpers import *


def distance(pos):
    return (abs(pos.x) + abs(pos.x + pos.y) + abs(pos.y)) // 2


# https://www.redblobgames.com/grids/hexagons/#neighbors-axial
directions = {
    'n': Vector2D(0, -1),
    'ne': Vector2D(1, -1),
    'se': Vector2D(1, 0),
    's': Vector2D(0, 1),
    'sw': Vector2D(-1, 1),
    'nw': Vector2D(-1, 0)
}

if __name__ == '__main__':
    paths = import_input('\n', example=False)
    for path in paths:
        path = path.split(',')
        position = Vector2D(0, 0)
        distances = []
        print('\t', 0, position)
        for direction in path:
            position += directions[direction]
            dist = distance(position)
            distances.append(dist)
            print(direction, '\t', dist, position)
        print(f"The shortest path is {color_text(distances[-1], 32)} tiles long.")
        print(f"The furthest distance recorded was {color_text(max(distances), 32)} tiles away.")
