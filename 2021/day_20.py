# Day 20 of Advent of Code 2021
# Trench Map

# With the scanners fully deployed, we turn their attention to mapping the floor of the ocean trench. When we get back
# the image from the scanners, it seems to just be random noise. Perhaps we can combine an image enhancement
# algorithm and the input image to clean it up a little.

# The image enhancement algorithm describes how to enhance an image by simultaneously converting all pixels in the input
# image into an output image. Each pixel of the output image is determined by looking at a 3x3 square of pixels centered
# on the corresponding input image pixel.

# Through advances in imaging technology, the images being operated on here are infinite in size. Every pixel of the
# infinite output image needs to be calculated exactly based on the relevant pixels of the input image. The small input
# image you have is only a small region of the actual infinite input image; the rest of the input image consists of
# dark pixels. We can keep enhancing our input image by running the result through the same image enhancement algorithm
# until we are satisfied with the result.

import matplotlib.pyplot as plt
import numpy as np

from aoc.helpers import *

if __name__ == "__main__":
    algorithm, input_image = import_input("\n\n")
    algorithm = np.array([char == "#" for char in algorithm])
    input_image = np.array([[char == "#" for char in line] for line in input_image.split("\n")])

    n = 50
    enhanced_image = input_image.copy()
    for step in range(n):
        # to make sure we also apply our filter to the outermost pixels of the "infinite" image we pad the image
        # with 0's or alternating 1's and 0's in case the index 0 of the enhancement algorithm is not a dark pixel.
        padded_image = np.pad(enhanced_image, 2, constant_values=(algorithm[0] == 1 and step % 2))
        new_image = np.zeros_like(padded_image)
        x_max, y_max = padded_image.shape
        for x, y in np.ndindex(*padded_image.shape):
            # Find the neighbours and flatten the three rows to one binary string to convert to an integer index.
            conv = padded_image[max(x - 1, 0) : min(x + 2, x_max), max(y - 1, 0) : min(y + 2, y_max)].flatten()
            idx = int("".join([str(bit) for bit in conv.astype(int)]), 2)
            # Apply the new pixel to the enhanced image.
            new_pixel = algorithm[idx]
            new_image[x, y] = new_pixel
        # cut off the unused padding to keep the image as small as possible.
        enhanced_image = new_image[1:-1, 1:-1]
        print("step:", step + 1, "| number of lights:", np.sum(enhanced_image))

    fig, (ax1, ax2) = plt.subplots(1, 2, sharex="all", sharey="all")
    diff = (np.array(enhanced_image.shape[0]) - np.array(input_image.shape)) // 2
    ax1.imshow(np.pad(input_image, diff))
    ax1.set_title("Input Image", fontsize=14, weight="bold")
    ax2.imshow(enhanced_image)
    ax2.set_title(f"After {n} Steps", fontsize=14, weight="bold")
    plt.show()
