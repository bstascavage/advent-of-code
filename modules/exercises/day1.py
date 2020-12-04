"""Advent of Code Day 1 module.

This module is used to solved Day 1's problem for the Advent of Code.
You can find the problem here:

https://adventofcode.com/2020/day/1

"""
# pylint: disable=import-error
from modules.helper import Helper


class Day1:
    """This class is an object for the Day 1 problem.

    This class loads an expense report file and does various comparasions.

    Args:
        expense_file (str): Path to the expense report file.

    Attributes:
        expense_list (str): Post-processed list of expenses (each element is an int.)

    """

    def __init__(self, expense_file):
        self.expense_list = Helper.load_file(expense_file)
        self.expense_list = [int(i) for i in self.expense_list]

    def expense_compare_two(self, value):
        """Loops through a list of integers.
        If two values sum up to the value, return their multiplication product.

        Args:
            input_list (list): A list of integers.
            value (int): An integer that the two integers should equal.
        Returns:
            The multiplication product of the two integers whose sum equals the provided value.
            If no integers can be found, returns None.
        """
        # Sets the list as a set for o(1) lookup of keys
        expenses = set(self.expense_list)

        for expense in self.expense_list:
            if value - expense in expenses:
                return expense * (value - expense)

        return None

    def expense_compare_three(self, value):
        """Loops through a list of integers.
        If three values sum up to the value, return their multiplication product.

        Args:
            input_list (list): A list of integers.
            value (int): An integer that the three integers should equal.
        Returns:
            The multiplication product of the three integers whose sum equals the provided value.
            If no integers can be found, returns None.
        """
        expenses = set(self.expense_list)
        for first_expense in self.expense_list:
            for second_expense in self.expense_list:
                if value - first_expense - second_expense in expenses:
                    return first_expense * second_expense * (value - first_expense - second_expense)

        return None
