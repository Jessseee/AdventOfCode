# Day 4 of Advent of Code 2021
# Giant Squid
from helpers import *
import re


def play(boards, num):
    completed = []
    for board in boards:
        for row in board:
            if num in row:
                row[row.index(num)] = False
        if any([not any(row) for row in board]) or any([not any(col) for col in list(zip(*board))]):
            print(sum(sum(board, [])) * num)
            completed.append(board)
    for board in completed:
        boards.remove(board)
    return boards


if __name__ == '__main__':
    inputs = import_input().read().split('\n\n')
    numbers = [int(num) for num in inputs[0].split(',')]
    boards = [[[int(num) for num in re.findall('.. ?', line)] for line in board.split('\n')] for board in inputs[1:]]
    for num in numbers:
        boards = play(boards, num)
