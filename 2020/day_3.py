# Day 3 Advent of Code
# Toboggan plane trajectory
import numpy as np

from aoc.helpers import color_text

file_name = "input/input_day_3.txt"


def check_trajectory_for_trees(right, down, print_trajectory=False):
    """
    :param int right: Number of steps to the right
    :param int down: Number of steps down

    :param bool print_trajectory: Print the trajectory to console
    :return: Number of trees encountered on the given trajectory
    """

    x = 0
    y = 0
    tree_count = 0

    with open(file_name) as f:
        for line in f.readlines():
            # for some reason Python doesn't print all the dots, so replace them with underscores
            line = line.replace(".", "_")

            if y != down and print_trajectory:
                print(line)
            else:
                # keep the x position within the width of the given lines
                x = (x + right) % (len(line) - 1)

                if line[x] == "#":
                    tree_count += 1
                    if print_trajectory:
                        print(f'{line[:x]}{c("X", 31)}{line[x + 1:]}')
                elif print_trajectory:
                    print(f"{line[:x]}O{line[x + 1:]}")
                y = 0
            y += 1
    f.close()

    print(f"number of trees in trajectory {right, down}: {c(tree_count, 31)}")
    return tree_count


if __name__ == "__main__":
    prod_of_trees_encountered = np.prod(
        (
            check_trajectory_for_trees(1, 1, True),
            check_trajectory_for_trees(3, 1),
            check_trajectory_for_trees(5, 1),
            check_trajectory_for_trees(7, 1),
            check_trajectory_for_trees(1, 2),
        )
    )
    print(f"the product of all trees encountered: {c(prod_of_trees_encountered, 31)}")
