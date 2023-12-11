# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
import numpy as np

from aoc.helpers import *


def reallocate_till_known_state(init_state):
    cycles = 0
    cur_state = init_state
    prev_states = []
    while tuple(cur_state) not in prev_states:
        prev_states.append(tuple(cur_state))
        cur_state = reallocate(cur_state)
        cycles += 1
    return cycles, cur_state


def reallocate(init_state):
    overloaded = np.argmax(init_state)
    to_reallocate = init_state[overloaded]

    new_state = init_state.copy()
    new_state[overloaded] = 0
    i = overloaded
    while to_reallocate > 0:
        i = (i + 1) % len(new_state)
        new_state[i] += 1
        to_reallocate -= 1
    return new_state


if __name__ == "__main__":
    init_state = np.array(import_input("\t", int))

    cycles, state = reallocate_till_known_state(init_state)
    print(f"It took {c(cycles, 32)} cycles to reallocate memory. Final state: {tuple(state)}")

    cycles, state = reallocate_till_known_state(state)
    print(f"The reallocation loop after state {tuple(state)} is {c(cycles, 32)} cycles long.")
