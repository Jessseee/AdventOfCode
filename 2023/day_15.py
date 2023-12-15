# Day 15 of Advent of Code 2023
# Lens Library

# As we approach the largest mountain on Lava Island, the newly-focused parabolic reflector dish directs all
# collected light to a facility embedded in the mountainside. Upon finding the entrance marked "Lava Production
# Facility" with a warning about personal protective equipment, we are greeted by a panicked reindeer inside. After
# gearing up with goggles and hard hats, the reindeer guides us through the facility. Entering the room that collects
# external light, we admire an array of lenses while the reindeer hands us a book titled "Initialization Manual." The
# book cheerfully instructs us to bring the Lava Production Facility online without unintended damage, mentioning the
# use of the Holiday ASCII String Helper (HASH) algorithm. we confirm that our HASH algorithm is operational by
# checking the sum of the hashed initialization sequence. The manual then details a series of 256 numbered boxes,
# each with lens slots and panels for lens adjustments. Alongside the boxes, a library contains lenses organized by
# focal length. The book proceeds to explain the Holiday ASCII String Helper Manual Arrangement Procedure (HASHMAP),
# outlining steps based on lens labels and corresponding HASH algorithm results. Our task is to find the correct
# arrangement of lenses based on the HASHMAP.


from collections import defaultdict

from aoc.helpers import *


def hash(string):
    return reduce(lambda acc, cur: ((acc + ord(cur)) * 17) % 256, string, 0)


def sort_lenses(init_sequence):
    boxes = defaultdict(dict)
    for step in init_sequence:
        if step.endswith("-"):
            label = step[:-1]
            hashed = hash(label)
            if label in boxes[hashed]:
                del boxes[hashed][label]
        else:
            label, focal_length = step.split("=")
            boxes[hash(label)][label] = int(focal_length)
    focus_power = 0
    for i, box in boxes.items():
        for j, (label, value) in enumerate(box.items(), 1):
            focus_power += (i + 1) * j * value
    return focus_power


if __name__ == "__main__":
    init_sequence = import_input(",", example=False)
    print("Sum of hashed initialization steps:", c(sum(hash(step) for step in init_sequence), Color.GREEN))
    print("Total focus power of lens configuration:", sort_lenses(init_sequence))
