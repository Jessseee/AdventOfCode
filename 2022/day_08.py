# Day 8 of Advent of Code 2022
# Treetop Tree House

# The expedition comes across a peculiar patch of tall trees carefully planted in a grid. It happens
# to be a reforestation afford of the previous expedition. It seems like a great location for a tree
# house. Our job is to first find a tree with enough cover to be hidden from the outside of the grid.
# We first count the number of visible trees. However, we also want a scenic view. So, next we grade
# each tree with a scenic score and build our tree house in the most scenic tree.

from helpers import *
import numpy as np


if __name__ == '__main__':
    forest = np.array(import_input('\n', lambda line: [int(char) for char in line], example=False))
    directions = Vector2D.directions()

    def look_in_direction(position, height, direction):
        visible = True
        trees = 0
        neighbour = Vector2D(*position) - direction
        while 0 <= neighbour.x < forest.shape[0] and 0 <= neighbour.y < forest.shape[1]:
            trees += 1
            if forest[neighbour.x, neighbour.y] >= height:
                visible = False
                break
            neighbour = neighbour - direction
        return visible, trees

    def grade_tree(position, height):
        scenic_score = 1
        visible = False
        for direction in directions:
            visible_in_direction, trees_in_direction = look_in_direction(position, height, direction)
            scenic_score *= trees_in_direction
            if visible_in_direction:
                visible = True
        return visible, scenic_score

    visible_trees = 0
    scenic_scores = []
    for position, height in np.ndenumerate(forest):
        visible, scenic_score = grade_tree(position, height)
        if visible: visible_trees += 1
        scenic_scores.append(scenic_score)
    top_scenic_score = max(scenic_scores)

    print(result(visible_trees), "trees are visible from the edge of the forest.")
    print("The highest scenic score of any tree:", result(top_scenic_score))

