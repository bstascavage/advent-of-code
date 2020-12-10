"""Advent of Code Day 9 module.

This module is used to solved Day 9's problem for the Advent of Code.
You can find the problem here:

https://adventofcode.com/2020/day/9

"""
# pylint: disable=import-error, no-name-in-module
import itertools
from modules.helper import Helper


class Day9:
    """This class is an object for the Day 9 problem.

    This class loads a list of integers as part of its fictional XMAS cypher protocol.

    Args:
        xmas_file (str): Path to the list of XMAS integers.

    Attributes:
        xmas_data (str): Array of XMAS integers.

    """

    def __init__(self, xmas_file):
        self.xmas_data = []
        temp_data = Helper.load_file(xmas_file)

        for elem in temp_data:
            self.xmas_data.append(int(elem))

    def find_first_wrong_number(self, premble_length):
        """Finds the first number in the list of ints who is not the sum of
        any numbers in the preamble.  When a number is a sum of any two numbers
        in the preamble, it is added to the end of the preamble and the first item
        of the preamble is removed.

        Args:
            preamble_length (int): Length of the preamble.
        Returns:
            The first number who is not the sum of any two items of the preamble.
        """
        preamble = self.xmas_data[:premble_length]
        remaining = self.xmas_data[premble_length:]

        while len(remaining) > 0:
            found = False
            sum_check = remaining.pop(0)

            for i in itertools.combinations(preamble, 2):
                if i[0] + i[1] == sum_check:
                    found = True
            if found:
                preamble.pop(0)
                preamble.append(sum_check)
            else:
                return sum_check

    def find_contiguous(self, check_answer):
        """Finds a contiguous set of numbers in the xmas data who sums is the
        given number.

        Args:
            check_answer (int): Integer to check the contiguous sum of.
        Returns:
            The sum of the smallest and largest number in the contiguous set.
        """

        for i, j in itertools.combinations(range(len(self.xmas_data) + 1), 2):
            if sum(self.xmas_data[i:j]) == check_answer:
                return min(self.xmas_data[i:j]) + max(self.xmas_data[i:j])

        return None
