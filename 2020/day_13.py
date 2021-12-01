# Day 13 Advent of Code
# Shuttle bus schedules
from helpers import *


def catch_first_bus(cur_time, schedule):
    for col in schedule:
        if col != 'x':
            if cur_time % col == 0:
                print(f'timestamp: {cur_time}, bus: {col}')
                return (cur_time-earliest_timestamp)*col
    return catch_first_bus(cur_time + 1, schedule)


def calculate_schedule_start_time(start_time, schedule):
    cur_time = start_time
    increment = 1
    for i, col in enumerate(schedule):
        if col == 'x':
            continue
        while (cur_time + i) % col != 0:
            cur_time += increment
        increment *= col
    return cur_time


if __name__ == '__main__':
    earliest_timestamp, schedule = import_input().read().split('\n')
    earliest_timestamp = int(earliest_timestamp)
    schedule = [int(col) if col.isdigit() else col for col in schedule.split(',')]

    print(f'First possible departure time: {catch_first_bus(earliest_timestamp, schedule)}')
    print(f'Ideal schedule start time: {calculate_schedule_start_time(1, schedule)}')



