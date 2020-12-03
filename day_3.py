# Day 3 Advent of Code
# Toboggan plane trajectory
from helpers import color_text
import numpy as np

file_name = "input/input_day_3.txt"


def check_trajectory_for_trees(right, down, print_trajectory=False):
    """
    Parameters:
        right (int): Number of steps to the right
        down (int): Number of steps down
        print_trajectory (bool): Print the trajectory to console
    Returns:
        int: Number of trees encountered on given trajectory
    """

    x = 0
    y = 0
    tree_count = 0

    with open(file_name) as f:
        for line in f.readlines():
            # for some reason Python doesn't print all the dots, so replace them with underscores
            line = line.replace('.', '_')

            if y != down and print_trajectory:
                print(line)
            else:
                # keep the x position within the width of the given lines
                x = (x + right) % (len(line) - 1)

                if line[x] == '#':
                    tree_count += 1
                    if print_trajectory:
                        print(f'{line[:x]}{color_text("X", 31)}{line[x + 1:]}')
                elif print_trajectory:
                    print(f'{line[:x]}O{line[x + 1:]}')
                y = 0
            y += 1
    f.close()

    print(f'number of trees in trajectory {right, down}: {color_text(tree_count, 31)}')
    return tree_count


if __name__ == '__main__':
    prod_of_trees_encountered = np.prod((
        check_trajectory_for_trees(1, 1, True),
        check_trajectory_for_trees(3, 1),
        check_trajectory_for_trees(5, 1),
        check_trajectory_for_trees(7, 1),
        check_trajectory_for_trees(1, 2)
    ))
    print(f'the product of all trees encountered: {color_text(prod_of_trees_encountered, 31)}')
