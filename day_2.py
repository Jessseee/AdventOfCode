# Day 2 of Advent of Code
# Toboggan Corporation password policy checker
from helpers import color_text
file_name = "input/input_day_2.txt"


# Part one
def sled_rental_pswd_policy_checker():
    """
    Print the number of valid passwords according to the sled rental password policy
    """
    nr_of_valid_passwords = 0
    with open(file_name) as f:
        for line in f.readlines():
            min_char, max_char, char, password = dissect_line(line)
            if max_char >= password.count(char) >= min_char:
                nr_of_valid_passwords += 1
    print(f'according to sled rental password\'s policy: {color_text(nr_of_valid_passwords, 31)}')


# Part two
def toboggan_corp_pswd_policy_checker():
    """
        Print the number of valid passwords according to Toboggan Corporation's password policy
    """
    nr_of_valid_passwords = 0
    with open(file_name) as f:
        for line in f.readlines():
            first_char, second_char, char, password = dissect_line(line)
            chars = password[first_char]+password[second_char]
            if chars.count(char) == 1:
                nr_of_valid_passwords += 1
    print(f'according to Toboggan Corporation\'s password policy: {color_text(nr_of_valid_passwords, 31)}')


def dissect_line(line):
    """
    :param str line: The line to be dissected
    :returns: The dissected policy and password
    """
    policy, password = line.split(':')
    limits, char = policy.split(' ')
    first_limit, second_limit = limits.split('-')
    return int(first_limit), int(second_limit), chr(char), str(password)


if __name__ == '__main__':
    print(f'Number of valid passwords in "{file_name}"')
    sled_rental_pswd_policy_checker()
    toboggan_corp_pswd_policy_checker()
