# Day 4 of Advent of Code 2021
# Giant Squid

# We found ourselves a squid friend, and they want to play bingo!
# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers.
# Numbers are chosen at random, and the chosen number is marked on all boards on
# which it appears. If all numbers in any row or any column of a board are marked,
# that board wins. (Diagonals don't count.) The submarine's bingo subsystem has
# given us a series of random numbers and bingo cards.

# It is our job to find out when which bingo card will win.
# We can either give the giant squid the first winning card or the last.
# depending on if we want to make friend.


from helpers import *
import re


if __name__ == '__main__':
    inputs = import_input('\n\n')
    numbers = [int(num) for num in inputs[0].split(',')]
    boards = [[[int(num) for num in re.findall('.. ?', line)] for line in board.split('\n')] for board in inputs[1:]]

    for num in numbers:
        completed = []
        for board in boards:
            for row in board:
                if num in row:
                    # mark the number by setting the value to False.
                    row[row.index(num)] = False
            # Check if any row or column do not have any 'truthy' values.
            if any([not any(row) for row in board]) or any([not any(col) for col in list(zip(*board))]):
                print_2d_array(board, 2)
                print(f'Board score: {sum(sum(board, [])) * num}')
                completed.append(board)
        for board in completed:
            boards.remove(board)
