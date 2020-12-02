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

    # Ensuring that every element in the list is set as an int
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
    input_list.sort()

    for first_entry in input_list:
        # Since list is sorted, if double the current element is greater than the value,
        # then we know that we couldn't find the value and should exit.
        if (first_entry*2) < value:
            for second_entry in input_list:
                if first_entry == second_entry:
                    continue
                if (first_entry+second_entry) == value:
                    return first_entry * second_entry
                # Since list is sorted, if this conditional happens
                # we can break out of the second loop
                if (first_entry+second_entry) > value:
                    break

        return None


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
    input_list.sort()

    for first_entry in input_list:
        for second_entry in input_list:
            # Since list is sorted, we can discard any entries
            # if the first and second would be greater than the value
            # regardless of what the third element is.
            # We can also skip if the first and second entries are equal.
            if (first_entry + second_entry + second_entry) >= value or first_entry == second_entry:
                break
            for third_entry in input_list:
                if third_entry in (first_entry, second_entry):
                    continue
                if (first_entry + second_entry + third_entry) == value:
                    return first_entry * second_entry * third_entry
                # Since list is sorted, if this conditional happens
                # we can break out of the third loop
                if (first_entry + second_entry + third_entry) > value:
                    break

    return None


if __name__ == "__main__":
    main()
