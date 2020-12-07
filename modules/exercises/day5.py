"""Advent of Code Day 5 module.

This module is used to solved Day 5's problem for the Advent of Code.
You can find the problem here:

https://adventofcode.com/2020/day/5

"""
# pylint: disable=import-error, too-few-public-methods
from modules.helper import Helper


class Day5:
    """This class is an object for the Day 5 problem.

    This class loads a list of boarding passes from a file and does various search functions.

    Args:
        boading_pass_file (str): Path to the list of boarding passes file.

    Attributes:
        boarding_passes (str): Post-processed array of boarding passes.

    """

    def __init__(self, boading_pass_file):
        self.boarding_passes = []

        for boarding_pass in Helper.load_file(boading_pass_file):
            # The boarding pass format is just binary, so we can subsitute these characters:
            # F = 0
            # B = 1
            # L = 0
            # R = 1
            self.boarding_passes.append(int(boarding_pass.replace("F", "0").replace(
                "B", "1").replace("L", "0").replace("R", "1"), 2))

    def get_highest_seat(self):
        """Finds the highest seat ID from a list of boarding passes

        Returns:
            The highest seat ID
        """

        # The challenge says to calculate (row * 5 + seat), but that just converts it to an int.
        # We already did this in the constructor.
        return max(self.boarding_passes)

    def find_missing_seat(self):
        """Looks through the list of boarding passes for a seat that is missing.
        If there is a seat 8 and a seat 10 in the list, this would return seat 9.

        Returns:
            The missing seat.
        """
        self.boarding_passes.sort()

        for index, item in enumerate(self.boarding_passes):
            if index == len(self.boarding_passes) - 1:
                break
            if abs(self.boarding_passes[index+1] - item) == 2:
                return item + 1
        return None
