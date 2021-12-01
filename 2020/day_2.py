# Day 2 of Advent of Code
# Toboggan Corporation password policy checker
from helpers import *


# Part one
def sled_rental_pswd_policy_checker(lines):
    """
    Print the number of valid passwords according to the sled rental password policy
    """
    nr_of_valid_passwords = 0
    for line in lines:
        min_char, max_char, char, password = dissect_line(line)
        if max_char >= password.count(char) >= min_char:
            nr_of_valid_passwords += 1
    return nr_of_valid_passwords


# Part two
def toboggan_corp_pswd_policy_checker(lines):
    """
        Print the number of valid passwords according to Toboggan Corporation's password policy
    """
    nr_of_valid_passwords = 0
    for line in lines:
        first_char, second_char, char, password = dissect_line(line)
        if (password[first_char] == char) is not (password[second_char] == char):
            nr_of_valid_passwords += 1
    return nr_of_valid_passwords


def dissect_line(line):
    """
    :param str line: The line to be dissected
    :returns: The dissected policy and password
    """
    policy, password = line.split(':')
    limits, char = policy.split(' ')
    first_limit, second_limit = map(int, limits.split('-'))
    return first_limit, second_limit, char, password


if __name__ == '__main__':
    lines = import_input().readlines()
    print(f'Number of valid passwords:\n'
          f'According to sled rental password\'s policy: '
          f'{color_text(sled_rental_pswd_policy_checker(lines), 31)}\n'
          f'According to Toboggan Corporation\'s password policy: '
          f'{color_text(toboggan_corp_pswd_policy_checker(lines), 31)}')
