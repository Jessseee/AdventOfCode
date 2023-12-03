# Day 15 Advent of Code
# Memory games
from aoc.helpers import *


def play_memory_game(start_numbers, number_of_turns):
    previous = {number: i + 1 for i, number in enumerate(start_numbers)}
    turn = len(previous)
    number = int(start_numbers[-1])
    while turn < number_of_turns:
        if not previous.get(number, None):
            previous[number] = turn
            number = 0
        else:
            last_seen = previous[number]
            previous[number] = turn
            number = turn - last_seen
        turn += 1
        print(f"{turn} \t {number}")


if __name__ == "__main__":
    start_numbers = [int(i) for i in import_input().read().split(",")]
    play_memory_game(start_numbers, 2020)
    play_memory_game(start_numbers, 30000000)
