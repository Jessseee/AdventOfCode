# Day 4 Advent of Code
# Passport validation
import re
from helpers import color_text

file_name = "input/input_day_4.txt"


def passport_scanner(required_keys):
    """
    :param required_keys: A tuple of required passport fields and regex to validate the field values
    :return: Lists of valid and invalid passports
    """
    valid_passports = []
    invalid_passports = []
    with open(file_name) as f:
        passport = {}
        for line in f.readlines():
            if line != "\n":
                key_value_pairs = line.split(' ')
                for pair in key_value_pairs:
                    key, value = pair.split(':')
                    # Remove the possible newline from end of field value
                    passport[key] = value.replace('\n', '')
            else:
                if validate_passport(passport, required_keys):
                    valid_passports.append(passport)
                else:
                    invalid_passports.append(passport)
                passport = {}
    f.close()
    return valid_passports, invalid_passports


def validate_passport(passport, required_keys):
    """
    :param passport: The passport to validate
    :param required_keys: A tuple of the required fields and regex to validate the field values
    :return: If all passport fields are present and valid
    """
    if all(key in passport for key in required_keys):
        for key, value in required_keys.items():
            if value != '':
                regex = re.compile(value)
                if not regex.match(passport[key]):
                    return False
        return True
    else:
        return False


if __name__ == '__main__':
    required_keys = {
        'pid': r'\b\d{9}\b',
        'byr': r'19[2-9]\d|200[0-2]',
        'iyr': r'20(1\d|20)',
        'eyr': r'20(2\d|30)',
        'hgt': r'1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in',
        'hcl': r'#[0-9a-f]{6}',
        'ecl': r'amb|blu|brn|gry|grn|hzl|oth'
    }

    valid_passports, invalid_passports = passport_scanner(required_keys)

    print(color_text(f'{len(invalid_passports)} invalid passports:', 31))
    for invalid_passport in invalid_passports:
        for key in required_keys:
            if key in invalid_passport:
                print(f'{key}: {invalid_passport[key]} |', end=' ')
        print('\n')

    print(color_text(f'\n{len(valid_passports)} valid passports:', 32))
    for valid_passport in valid_passports:
        for key in required_keys:
            print(f'{key}: {valid_passport[key]} |', end=' ')
        print('\n')
