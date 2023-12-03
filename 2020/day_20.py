# Day  20 Advent of Code
import numpy as np

from aoc.helpers import *


class Image:
    def __init__(self, img_id, array):
        self.img_id = img_id
        self.array = array
        self.rot = 0
        self.edges = []
        self.position = (0, 0)
        for i in range(4):
            self.edges.append(list(array[0]))
            array = np.rot90(array)

    def compare_edge(self, other):
        for i in range(4):
            edge = list(np.rot90(self.array, i)[0])
            for j in range(4):
                other_edge = list(np.rot90(other.array, j)[0])
                if edge == other_edge:
                    other.rotate(2 - j)
                    return 2 - j
                elif edge == other_edge[::-1]:
                    other.rotate(2 - j)
                    other.flip(j % 2)
                    return 2 - j
        return False

    def rotate(self, rot):
        self.array = np.rot90(self.array)
        self.rot += self.rot + rot % 4

    def flip(self, dir):
        self.array = np.flip(self.array, dir)


def find_matching_images(image, images, placed):
    print([[image.img_id, image.position] for image in placed.values()])
    matching_images = []
    for other in [other for other in images.values() if other is not image]:
        if rot_diff := image.compare_edge(other):
            matching_images.append((rot_diff, other))

    for rot_diff, other in matching_images:
        other.position = (image.position[0] + DIRS[rot_diff][0], image.position[1] + DIRS[rot_diff][1])
        placed[other.img_id] = other
        del images[other.img_id]
        find_matching_images(other, images, placed)


if __name__ == "__main__":
    IMG_SIZE = 10
    DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    images = import_input(True).read().replace("#", "1").replace(".", "0").split("\n\n")
    images = {
        int(id.split(" ")[1]): Image(
            int(id.split(" ")[1]), np.array([[int(char) for char in line] for line in image.split("\n")])
        )
        for id, image in [data.split(":\n") for data in images]
    }
    find_matching_images(images[1427], images, {})
