# Day 2 of Advent of Code 2022
# Rock Paper Scissors

# To determine who may sleep closes to the snack storage the Elves hold a Rock Paper Scissors tournament.
# As appreciation for our help yesterday one Elf hands us an encrypted strategy guide. Our task is to
# use these instructions to calculate the score we will have at the end of the tournament.
# Our total score is the sum of our scores for each round. The score for a single round is the score for the shape
# We selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
# (0 if we lost, 3 if the round was a draw, and 6 if we won). The instructions tell us exactly what our opponent
# will play and what we need to play in response to win the tournament without being too obvious.

from aoc.helpers import *


def rock_paper_scissors(instructions, results):
    score = 0
    for opponent, response in instructions:
        score += results[opponent][response]
    return score


if __name__ == "__main__":
    instructions = import_input("\n", lambda line: line.split(" "))

    results = {"A": {"X": 4, "Y": 8, "Z": 3}, "B": {"X": 1, "Y": 5, "Z": 9}, "C": {"X": 7, "Y": 2, "Z": 6}}
    print(
        "Using the interpreted strategy guide the tournament score is: ",
        c(rock_paper_scissors(instructions, results), Color.GREEN),
    )

    results = {"A": {"Y": 4, "Z": 8, "X": 3}, "B": {"X": 1, "Y": 5, "Z": 9}, "C": {"Z": 7, "X": 2, "Y": 6}}
    print(
        "Using the actual strategy guide the tournament score is: ",
        c(rock_paper_scissors(instructions, results), Color.GREEN),
    )
