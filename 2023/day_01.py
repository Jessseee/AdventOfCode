# Day 1 of Advent of Code 2023
# Trebuchet?!

# To inspect the sky for snow the Elves want to launch us with a trebuchet.
# However, their calibration document seems to be amended. The newly-improved
# document consists of lines of text that each contain a calibration value.
# Our task is to find the correct calibration values by combining the first
# and last digit in each line.

from helpers import *

digits = dict(one='1', two='2', three='3', four='4', five='5', six='6', seven='7', eight='8', nine='9')
pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"


def str_to_digit(string):
    return string if string.isdigit() else digits[string]


def parse_input(line):
    digits = list(map(str_to_digit, re.findall(pattern, line)))
    return int(digits[0] + digits[-1])


if __name__ == '__main__':
    inputs = import_input('\n', parse_input, example=False)
    print("The sum of all of the calibration values:", sum(inputs))
