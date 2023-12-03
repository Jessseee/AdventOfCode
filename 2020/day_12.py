# Day 12 Advent of Code
# Finding the way
from aoc.helpers import *


def move_boat_wrongly(boat, action):
    dir, amount = action[0], int(action[1:])
    if dir == "F":
        if boat[2] == 0:
            dir = "S"
        if boat[2] == 90:
            dir = "E"
        if boat[2] == 180:
            dir = "N"
        if boat[2] == 270:
            dir = "W"
    elif dir == "N":
        boat[1] -= amount
    elif dir == "S":
        boat[1] += amount
    if dir == "E":
        boat[0] -= amount
    elif dir == "W":
        boat[0] += amount
    elif dir == "L":
        boat[2] = (boat[2] + amount) % 360
    elif dir == "R":
        boat[2] = (boat[2] - amount) % 360
    print(action, boat)
    return boat


def move_boat_with_waypoint(boat, waypoint, action):
    dir, amount = action[0], int(action[1:])
    new_waypoint = waypoint.copy()
    print(f"{boat} {waypoint}\n{dir}{amount}")
    if dir == "F":
        boat[0] += amount * waypoint[0]
        boat[1] += amount * waypoint[1]
        return new_waypoint
    elif dir == "N":
        return [new_waypoint[0], new_waypoint[1] + amount]
    elif dir == "S":
        return [new_waypoint[0], new_waypoint[1] - amount]
    elif dir == "E":
        return [new_waypoint[0] + amount, new_waypoint[1]]
    elif dir == "W":
        return [new_waypoint[0] - amount, new_waypoint[1]]
    elif dir == "L":
        if amount == 90:
            return [-new_waypoint[1], new_waypoint[0]]
        elif amount == 180:
            return [-new_waypoint[0], -new_waypoint[1]]
        elif amount == 270:
            return [new_waypoint[1], -new_waypoint[0]]
    elif dir == "R":
        if amount == 90:
            return [new_waypoint[1], -new_waypoint[0]]
        elif amount == 180:
            return [-new_waypoint[0], -new_waypoint[1]]
        elif amount == 270:
            return [-new_waypoint[1], new_waypoint[0]]


if __name__ == "__main__":
    actions = import_input().read().split("\n")
    boat = [0, 0, 90]
    waypoint = [10, 1]
    for action in actions:
        if action:
            waypoint = move_boat_with_waypoint(boat, waypoint, action)
    print(abs(boat[0]) + abs(boat[1]))
