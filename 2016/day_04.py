# Day 4 of Advent of Code 2016
# Security Through Obscurity
from collections import Counter

from aoc.helpers import *


def parse(s):
    return (re.findall(r"(\w+)-", s), int(re.search(r"\d+", s).group()), re.search(r"\[(\w+)\]", s).group(1))


def check(encrypted_name, checksum):
    encrypted_name = sorted("".join(encrypted_name))
    letter_count = Counter(encrypted_name).most_common(5)
    return checksum == "".join([letter for letter, count in letter_count])


def decrypt_name(encrypted_name, shift):
    decrypted_name = ""
    for word in encrypted_name:
        for letter in word:
            shifted_letter = chr((ord(letter) - 97 + shift) % 26 + 97)
            decrypted_name += shifted_letter
        decrypted_name += " "
    return decrypted_name


if __name__ == "__main__":
    inputs = import_input("\n", parse, example=False)

    score = 0
    north_pole_room = ()
    for encrypted_name, sector_id, checksum in inputs:
        if check(encrypted_name, checksum):
            score += sector_id
            name = decrypt_name(encrypted_name, sector_id)
            if "northpole" in name:
                north_pole_room = (name, sector_id)
            print(c(f"{encrypted_name} {sector_id} {checksum}", Color.GREEN))
            print(name)
        else:
            print(c(f"{encrypted_name} {sector_id} {checksum}", Color.RED))
        print()

    print(f"The sum of the sector IDs of the valid rooms: {score}")
    print(f"The sector ID of the room of North Pole objects: {north_pole_room}")
