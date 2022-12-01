# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from helpers import *

keypad_one = """
123
456
789
"""

keypad_two = """
  1  
 234 
56789
 ABC 
  D  
"""

dirs = {'U': Matrix(-1, 0),
        'R': Matrix(0, 1),
        'D': Matrix(1, 0),
        'L': Matrix(0, -1)}


def parse_keypad(keypad):
    return [[x for x in row] for row in keypad.split('\n')[1:-1]]


def get_keypad_code(keypad, inputs, start_pos):
    keypad = parse_keypad(keypad)
    print('keypad:')
    print_2d_array(keypad)
    print('code: ', end='')
    pos = start_pos
    for line in inputs:
        for key in line:
            new_pos = pos + dirs[key]
            if 0 <= new_pos[0] <= len(keypad)-1 and 0 <= new_pos[1] <= len(keypad[0])-1:
                if keypad[new_pos[0]][new_pos[1]] != ' ':
                    pos = new_pos
        print(color_text(keypad[pos[0]][pos[1]], Color.GREEN), end='')
    print('\n')


if __name__ == '__main__':
    inputs = import_input('\n', lambda x: [c for c in x], example=False)

    get_keypad_code(keypad_one, inputs, Matrix(1, 1))
    get_keypad_code(keypad_two, inputs, Matrix(2, 0))
