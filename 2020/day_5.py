# Day 5 Advent of Code
# Finding my plane seat
from aoc.helpers import color_text

file_name = "input/input_day_5.txt"
plane_rows = 128
plane_columns = 8


def check_boarding_passes():
    """
    :return: Dictionary of boarding passes with seat IDs and encoded seat locations
    """
    boarding_passes = {}
    with open(file_name) as f:
        for boarding_pass in f.readlines():
            boarding_pass = boarding_pass.rstrip("\n")  # strip off newline character
            seat_id = decode_boarding_pass(boarding_pass)
            boarding_passes[seat_id] = boarding_pass
    f.close()
    return boarding_passes


def decode_boarding_pass(boarding_pass):
    """
    :param boarding_pass: A boarding pass's encoded seat location
    :return: Seat ID (row * 8 + column)
    """
    min_row = 0
    max_row = plane_rows - 1
    min_column = 0
    max_column = plane_columns - 1

    for char in boarding_pass:
        current_range_row = max_row - min_row + 1
        current_range_column = max_column - min_column + 1
        if char == "F":
            max_row -= current_range_row // 2
        elif char == "B":
            min_row += current_range_row // 2
        elif char == "L":
            max_column -= current_range_column // 2
        elif char == "R":
            min_column += current_range_column // 2
    row = min_row
    column = min_column
    seat_id = row * 8 + column
    return seat_id


def find_missing_seat_ids(boarding_passes):
    """
    :param boarding_passes: Dictionary of boarding passes with seat IDs and encoded seat locations
    :return: A list of seat IDs missing from the middle of the dictionary
    """
    missing_seat_ids = []
    min_seat_id = min(boarding_passes)
    max_seat_id = max(boarding_passes)
    for seat_id in range(min_seat_id, max_seat_id):
        if seat_id not in boarding_passes:
            missing_seat_ids.append(seat_id)
    return missing_seat_ids


if __name__ == "__main__":
    boarding_passes = check_boarding_passes()
    print(f"The highest seat ID: {c(max(boarding_passes), 31)}")
    missing_seat_ids = find_missing_seat_ids(boarding_passes)
    print(f"Missing seat ID(s):\n{missing_seat_ids}")
