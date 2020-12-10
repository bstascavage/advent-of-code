"""Advent of Code Day 6 module.

This module is used to solved Day 6's problem for the Advent of Code.
You can find the problem here:

https://adventofcode.com/2020/day/6

"""
# pylint: disable=import-error, no-name-in-module
from modules.helper import Helper


class Day6:
    """This class is an object for the Day 6 problem.

    This class loads a list of questionaire form answer from a file
    and does various search functions.

    Args:
        form_file (str): Path to the list of questionaire form answer file.

    Attributes:
        answers (str): Post-processed 2D array of questionaire answers.

    """

    def __init__(self, form_file):
        self.answers = []

        # This logic split this horrible file into an array of dicts.
        # Since the delemeter is "double newline" instead of a single one,
        # we need to split on "\n\n".
        for line in Helper.load_file(form_file, "\n\n"):
            new_group = []

            # Each line in a group is it's own element.
            temp_group = line.split('\n')

            # Transforms the group into a list of sets, where each set is a person's
            # answers.
            for person in temp_group:
                new_group.append(set(person))

            self.answers.append(new_group)

    def count_unique_group_answers(self):
        """Counts the number of unique answers in each group.

        Returns:
            The sum of the number of unique answers for each group.
        """
        count = 0

        for group in self.answers:
            count += len(set.union(*group))

        return count

    def count_complete_group_answers(self):
        """Counts the number of answers by every person in a group.

        Returns:
            The number of questions everyone answered across all groups.
        """
        count = 0

        for group in self.answers:
            count += len(set.intersection(*group))

        return count
