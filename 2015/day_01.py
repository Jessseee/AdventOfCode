# Day 1 of Advent of Code 2015
# Not Quite Lisp
from helpers import *


if __name__ == '__main__':
    inputs = import_input(example=False).read()
    counter = 0
    for i, instruction in enumerate(inputs):
        counter += 1 if instruction == '(' else -1
        if counter == -1:
            print('santa enters the basement at instruction', i+1)
    print('final floor:', counter)

