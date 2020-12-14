# Day 13 Advent of Code
# Shuttle bus schedules
from helpers import *


def get_first_bus(cur_time, busses):
    for bus in busses:
        if bus != 'x':
            bus = int(bus)
            if cur_time % bus == 0:
                print(f'timestamp: {cur_time}, bus: {bus}')
                return (cur_time-earliest_timestamp)*bus
    return get_first_bus(cur_time+1, busses)


def get_schedule_start_time(start_time, schedule):
    cur_time = start_time
    increment = 1
    for i, bus in enumerate(schedule):
        if bus == 'x':
            continue
        bus = int(bus)
        while (cur_time + i) % bus != 0:
            cur_time += increment
        increment *= bus
    return cur_time


if __name__ == '__main__':
    earliest_timestamp, schedule = import_input().read().split('\n')
    earliest_timestamp = int(earliest_timestamp)
    schedule = [bus for bus in schedule.split(',')]

    print(get_first_bus(earliest_timestamp, schedule))
    print(get_schedule_start_time(1, schedule))



