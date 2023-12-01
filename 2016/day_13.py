# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from helpers import *
from math import inf


def is_wall(x, y, bias) -> bool:
    value = x * x + 3 * x + 2 * x * y + y + y * y
    value += bias
    value = sum(map(int, '{0:b}'.format(value)))
    return value % 2 != 0


def get_neighbours(x, y) -> list[tuple[int, int]]:
    neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(x, y) for x, y in neighbours if min(x, y) >= 0]


def dist(room1, room2) -> float:
    (x1, y1), (x2, y2) = room1, room2
    return abs(x1 - x2) + abs(y1 - y2)


def backtrack(current, path) -> list[tuple[int, int]]:
    shortest_path = []
    cur = current
    while cur != start:
        cur = path[cur]
        shortest_path.append(cur)
    return shortest_path


def search(start, target):
    current = start
    to_visit = {current}
    connections = {}
    observed = {current: 0}
    walls = []
    shortest_path = []

    while True:
        d = {room: observed[room] for room in to_visit}
        if len(d) == 0:
            break
        current = min(d, key=d.get)
        if current == target:
            shortest_path = backtrack(current, connections)
        to_visit.remove(current)
        for neighbour in get_neighbours(*current):
            if is_wall(*neighbour, bias):
                walls.append(neighbour)
                continue
            steps = observed[current] + 1
            if steps < observed.get(neighbour, inf):
                connections[neighbour] = current
                observed[neighbour] = steps
                if neighbour not in to_visit:
                    to_visit.add(neighbour)

    return observed, walls, shortest_path


def plot_search(start, target, observed, walls, shortest_path):
    plt.figure(figsize=(7, 7))
    plt.scatter(*zip(*observed), c="gray")
    plt.scatter(*zip(*walls), c="purple")
    if shortest_path:
        plt.scatter(*zip(*shortest_path), c="yellow")
    plt.scatter(*start, c="green")
    plt.scatter(*target, c="red")
    plt.show()


if __name__ == '__main__':
    bias = int(import_input(example=False).read())
    start = (1, 1)
    target = (31, 39)
    results = (observed, _, shortest_path) = search(start, target)

    print(f"Length of shortest path to room {target}:", len(shortest_path))
    print("number of rooms that can be visited in at most 50 steps: ",
          len([room for room, steps in observed.items() if steps <= 50]))

    plot_search(start, target, *results)

