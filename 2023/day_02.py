# Day 2 of Advent of Code 2023
# Cube Conundrum

# After being launched by the Elves we find ourselves on an island in the sky.
# An Elf explains that we arrived at Snow Island, however it is quite a walk
# to the snow production facilities. The Elf suggests we play a game on the
# way there. They show us a small bag with red, green and blue cubes. Three
# times per round of the game the Elf pulls out a number of cubes. Our goal is
# to find out which games are possible given a number of cubes in the bag and
# what the minimum number of cubes is that is required for a given game.

import numpy as np

from aoc.helpers import *


def parse_game(line):
    cubes = {}
    for n, c in [ball.split(" ") for ball in re.findall(r"(\d+ \w+)", line)]:
        cubes[c] = max(int(n), cubes.get(c, 0))
    return cubes


def validate_game(i, game):
    if any([number > bag[color] for color, number in game.items()]):
        return 0
    return i


if __name__ == "__main__":
    games = import_input("\n", parse_game)
    bag = dict(red=12, green=13, blue=14)
    valid_games = powers = 0
    for i, game in enumerate(games, start=1):
        valid_games += validate_game(i, game)
        powers += np.prod(list(game.values()))
    print("The sum of the valid game IDs:", c(valid_games, Color.GREEN))
    print("The power of the minimum cubes required each game:", c(powers, Color.GREEN))
