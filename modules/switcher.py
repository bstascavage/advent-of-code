"""Advent of Code main module.

This module is used to determine which 'day' module to use.  For more information:

https://adventofcode.com/2020/

"""
import importlib


class Switcher(object):
    """This class is an object for the Advent of Code challenge.

    This class loads a given day's module and runs each challenge's functions.

    Args:
        expense_name (str): Which day's challenge to run.

    Attributes:
        expense_app (obj): Dynamic class to run exercises on.

    """

    def __init__(self, exercise_name):
        module = importlib.import_module('.exercises', package='modules')
        exercise_class = getattr(module, exercise_name)
        self.exercise_app = exercise_class(
            "inputs/%s/input.txt" % exercise_name.lower())
        self.exercise_name = exercise_name

    def run_exercise(self):
        """Dynamically looks up given day's challenge functions.

        Returns:
            The results of the dynamic function.
        """
        function = getattr(self, self.exercise_name.lower(),
                           lambda: "Invalid function")
        return function()

    def print_results(self, answer_one=None, answer_two=None):
        """Takes in a day's answers and prints them pretty.

        Args:
            answer_one (str): Answer to Part 1.
            answer_two (str): Answer to Part 2.
        """
        print("********%s*******" % self.exercise_name)
        print("Part 1: %s" % answer_one)
        print("Part 2: %s" % answer_two)
        print("*******************")

    def day1(self):
        """Determines Day 1's anwsers."""
        part_one_answer = self.exercise_app.expense_compare_two(2020)
        part_two_answer = self.exercise_app.expense_compare_three(2020)

        self.print_results(part_one_answer, part_two_answer)

    def day2(self):
        """Determines Day 2's anwsers."""
        part_one_answer = self.exercise_app.count_valid_passwords_part1()
        part_two_answer = self.exercise_app.count_valid_passwords_part2()

        self.print_results(part_one_answer, part_two_answer)

    def day3(self):
        """Determines Day 3's anwsers."""

        # pylint: disable=line-too-long
        part_one_answer = self.exercise_app.find_trees_in_path(3, 1)
        part_two_answer = self.exercise_app.find_trees_in_path(1, 1) * self.exercise_app.find_trees_in_path(
            3, 1) * self.exercise_app.find_trees_in_path(5, 1) * self.exercise_app.find_trees_in_path(7, 1) * self.exercise_app.find_trees_in_path(1, 2)

        self.print_results(part_one_answer, part_two_answer)
