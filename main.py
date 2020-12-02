"""Advent of Code Programming Excercise

This module is the main module for the "Advent of Code" excersises (https://adventofcode.com/).
More information will be added as more functionality is added.

Example:
    $ python main.py

Attributes:
    <placeholder>
"""
import sys

EXPENSE_REPORT = "expense_report.txt"


def main():
    """Main function.

    Returns:
        True upon successful runs.
    """
    expense_list = load_file(EXPENSE_REPORT)

    # Ensuring that every element in the list is set as an int.
    # TODO: assumes all numbers are integers and are positive.  We should check this.
    expense_list = [int(i) for i in expense_list]

    print(expense_compare_two(expense_list, 2020))
    print(expense_compare_three(expense_list, 2020))

    return True


def load_file(file):
    """Loads text file into a list

    Args:
        file (str): Path of text file to load

    Returns:
        A list where every element is a line from the file.
    """
    try:
        input_file = open(file, "r")
        output_list = input_file.read().split("\n")
        input_file.close()
        return output_list
    except IOError:
        sys.exit("ERROR: Cannot load file: %s" % file)


def expense_compare_two(input_list, value):
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
    expenses = set(input_list)

    for expense in input_list:
        if value - expense in expenses:
            return expense * (value - expense)


def expense_compare_three(input_list, value):
    """Loops through a list of integers.
    If three values sum up to the value, return their multiplication product.

    Args:
        input_list (list): A list of integers.
        value (int): An integer that the three integers should equal.

    Returns:
        The multiplication product of the three integers whose sum equals the provided value.
        If no integers can be found, returns None.
    """
    expenses = set(input_list)
    for first_expense in input_list:
        for second_expense in input_list:
            if value - first_expense - second_expense in expenses:
                return first_expense * second_expense * (value - first_expense - second_expense)


if __name__ == "__main__":
    main()
