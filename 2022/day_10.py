# Day 10 of Advent of Code 2022
# Cathode-Ray Tube

# Unfortunately the communication device endured some water damage. It is our task to repair
# the broken cathode-ray tube display. The screen is also driven by a clock circuit which
# ticks at a constant rate; each tick is called a cycle. The CPU of the device contains a
# single register, X, which starts at value 1 and supports two instructions:
# - addx V: takes two cycles to complete after which the value V is added to register X
# - noop: takes one cycle to complete and has no other effect.
# Our job is to find out what the values of register X are during the execution of a given
# program and what the resulting image on the screen should look like.

from helpers import *


class AddX:
    def __init__(self, value):
        self.cycles = 2
        self.value = value

    def finished(self):
        while self.cycles > 1:
            self.cycles -= 1
            return False
        return True

    def __repr__(self):
        return f"addx {self.value}"


if __name__ == '__main__':
    instructions = import_input('\n', example=False)
    X = 1
    crt = []
    cycle = 1
    current_operation = None
    signal_strengths = []
    while len(instructions) > 0 or current_operation is not None:
        if current_operation is None and len(instructions) > 0:
            instruction = instructions.pop(0).split(' ')
            if instruction[0] == 'noop':
                print(f"Start cycle  {cycle}: begin executing noop")
                pass
            elif instruction[0] == 'addx':
                current_operation = AddX(int(instruction[1]))
                print(f"Start cycle  {cycle}: begin executing {current_operation}")

        if (cycle - 20) % 40 == 0 or cycle == 20:
            signal_strengths.append(cycle * X)

        pixel = (cycle - 1) % 40
        if pixel == 0:
            crt.append([])
        crt[-1].append(result('0') if pixel in range(X - 1, X + 2) else ' ')

        print(f"During cycle {cycle}: draw pixel in position {pixel}")
        print("Current CRT row:", ''.join(crt[-1]))

        if current_operation is not None and current_operation.finished():
            X += current_operation.value
            print(f"End of cycle {cycle}: finish executing {current_operation} (X is now {X})")
            current_operation = None

        cycle += 1
        print()

    print(f"The sum of the signal strengths is: {result(sum(signal_strengths))}\n")

    print("The final rendered image:")
    print_2d_array(crt)
