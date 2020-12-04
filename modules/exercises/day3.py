"""Advent of Code Day 3 module.

This module is used to solved Day 3's problem for the Advent of Code.
You can find the problem here:

https://adventofcode.com/2020/day/3

"""
# pylint: disable=import-error, too-few-public-methods
from modules.helper import Helper


class Day3:
    """This class is an object for the Day 3 problem.

    This class loads a toboggan map file and does various pathing functions.

    Args:
        map_file (str): Path to the toboggan map file.

    Attributes:
        map (str): Post-processed 2D array of toboggan map.

    """

    def __init__(self, map_file):
        self.map = []
        preprocessed_map = Helper.load_file(map_file)

        # Converting file into 2D array
        for line in preprocessed_map:
            self.map.append(list("".join([line])))

    def find_trees_in_path(self, right_mov, down_mov):
        """Starting at the top-left corner of the map, counts the number of trees in the path,
        where you move to the right by `right_move` amount, move down by `down_mov` amount, check
        to see if the space is a tree, and repeat.

        Args:
            right_mov (int): Number of spaces to transverse to the right.
            down_mov (int): Number of spaces to transverse down.

        Returns:
            The number of trees in the given path.
        """
        current_right = right_mov
        tree_count = 0

        # Looping through each row of the map, skipping every N rows, where N is down_mov-1
        for i in range(0, len(self.map), down_mov):
            # Need to skip index 0 since we start the count at 1
            if i == 0:
                continue

            # "Wrap-around" logic.  If current_right exceeds the size of the inner loop,
            # we need to reset it.
            if current_right > (len(self.map[i]) - 1):
                current_right = current_right - len(self.map[i])

            if self.map[i][current_right] == "#":
                tree_count += 1
            current_right += right_mov

        return tree_count
