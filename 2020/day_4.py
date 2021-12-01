# Day 4 Advent of Code
# Passport validation
import re
from helpers import *


def scan_passports(input, validate):
    """
    :param input: List of all unvalidated passports
    :param validate: Method to validate passports
    :return: Lists of valid and invalid passports
    """
    valid_passports = []
    invalid_passports = []

    for passport in input:
        key_value_pairs = passport.replace('\n', ' ').split(' ')
        passport = {}
        for pair in key_value_pairs:
            key, value = pair.split(':')
            passport[key] = value
        if validate(passport):
            valid_passports.append(passport)
        else:
            invalid_passports.append(passport)
    print_passports(valid_passports, invalid_passports)
    return valid_passports, invalid_passports


def validate_fields(passport):
    """
    :param passport: The passport to validate
    :return: If all passport fields are present and valid
    """
    if all(key in passport for key in REQUIRED_KEYS):
        for key, value in REQUIRED_KEYS.items():
            if value != '':
                regex = re.compile(value)
                if not regex.match(passport[key]):
                    return False
        return True
    return False


def check_required_fields(passport):
    """
    :param passport: The passport to validate
    :return: If all passport fields are present
    """
    return all(key in passport for key in REQUIRED_KEYS)


def print_passports(valid_passports, invalid_passports, print_all=False):
    """
    :param valid_passports: List of valid passports
    :param invalid_passports: List of invalid passports
    :param print_all: Should print all passport data
    :return:
    """
    print(f'valid passports: {color_text(len(valid_passports), 32)}')
    print(f'invalid passports: {color_text(len(invalid_passports), 31)}')
    if print_all:
        print(color_text('\nVALID PASSPORTS', 32))
        for valid_passport in valid_passports:
            for key in REQUIRED_KEYS:
                print(color_text(f'{key}: {valid_passport[key]} |', 37), end=' ')
            print('\n')
        print(color_text('\nINVALID PASSPORTS', 31))
        for invalid_passport in invalid_passports:
            for key in REQUIRED_KEYS:
                if key in invalid_passport:
                    print(color_text(f'{key}: {invalid_passport[key]} |', 37), end=' ')
            print('\n')


if __name__ == '__main__':
    REQUIRED_KEYS = {
        'pid': r'\b\d{9}\b',
        'byr': r'19[2-9]\d|200[0-2]',
        'iyr': r'20(1\d|20)',
        'eyr': r'20(2\d|30)',
        'hgt': r'1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in',
        'hcl': r'#[0-9a-f]{6}',
        'ecl': r'amb|blu|brn|gry|grn|hzl|oth'
    }
    passports = import_input().read().split('\n\n')
    print("Check required fields:")
    scan_passports(passports, check_required_fields)
    print("\nCheck required fields and validity:")
    scan_passports(passports, validate_fields)
