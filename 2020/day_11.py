# Day 11 Advent of Code
# Ferry chair dance
from aoc.helpers import *


def get_stable_seating(grid, seat_check, tolerance):
    new_grid = []
    for row in range(len(grid)):
        new_grid.append([])
        if not grid[row]:
            continue
        for col in range(len(grid[row])):
            seat = grid[row][col]
            if seat == GRID_CELL["floor"]:
                new_grid[row].append(seat)
                continue
            if seat == GRID_CELL["unoccupied"]:
                if seat_check(grid, [row, col]) == 0:
                    new_grid[row].append(GRID_CELL["occupied"])
                    continue
            elif seat == GRID_CELL["occupied"]:
                if seat_check(grid, [row, col]) >= tolerance:
                    new_grid[row].append(GRID_CELL["unoccupied"])
                    continue
            new_grid[row].append(seat)
    if grid != new_grid:
        return get_stable_seating(new_grid, seat_check, tolerance)
    else:
        return new_grid


def check_adjacent(grid, seat):
    occupied_seats = 0
    for dir in DIRS:
        pos = [seat[0] + dir[0], seat[1] + dir[1]]
        if 0 <= pos[0] < grid_size[0] and 0 <= pos[1] < grid_size[1]:
            if grid[pos[0]][pos[1]] == GRID_CELL["occupied"]:
                occupied_seats += 1
    return occupied_seats


def check_visible(grid, seat):
    occupied_seats = 0
    for dir in DIRS:
        pos = [seat[0] + dir[0], seat[1] + dir[1]]
        while 0 <= pos[0] < grid_size[0] and 0 <= pos[1] < grid_size[1]:
            cur_seat = grid[pos[0]][pos[1]]
            if cur_seat == GRID_CELL["occupied"]:
                occupied_seats += 1
                break
            elif cur_seat == GRID_CELL["unoccupied"]:
                break
            else:
                pos[0] += dir[0]
                pos[1] += dir[1]
    return occupied_seats


if __name__ == "__main__":
    DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    GRID_CELL = {"floor": 0, "unoccupied": 1, "occupied": 2}
    grid = (
        import_input()
        .read()
        .replace(".", str(GRID_CELL["floor"]))
        .replace("L", str(GRID_CELL["unoccupied"]))
        .split("\n")
    )
    grid = [[int(char) for char in row] for row in grid]
    grid_size = [len(grid), len(grid[0])]
    print(
        f"Tolerance 4 and only check adjacent seats\n" f"Total occupied seats:",
        sum([row.count(GRID_CELL["occupied"]) for row in get_stable_seating(grid, check_adjacent, 4)]),
    )
    print(
        f"Tolerance 5 and check nearest visible seats\n" f"Total occupied seats:",
        sum([row.count(GRID_CELL["occupied"]) for row in get_stable_seating(grid, check_visible, 5)]),
    )
