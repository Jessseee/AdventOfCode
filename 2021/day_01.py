from helpers import *


if __name__ == '__main__':
    inputs = [int(line.rstrip('\n')) for line in import_input('\n')]
    single_increases = sum(inputs[i] < inputs[i+1] for i in range(len(inputs)-1))
    print(f'There are {color_text(single_increases, 32)} increases in the single depth measurements.')
    sweep_increases = sum(sum(inputs[i:i+3]) < sum(inputs[i+1:i+4]) for i in range(len(inputs)-4))
    print(f'There are {color_text(sweep_increases, 32)} increases in the sliding window depth measurements.')
