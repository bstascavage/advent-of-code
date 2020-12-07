"""Advent of Code Day 6 module.

This module is used to solved Day 6's problem for the Advent of Code.
You can find the problem here:

https://adventofcode.com/2020/day/6

"""
# pylint: disable=import-error, too-few-public-methods
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
            self.answers.append(
                {'answers': line.replace('\n', ''), 'group_size': line.count('\n') + 1})

        print(self.answers)

    def count_unique_group_answers(self):
        """Counts the number of unique answers in each group.

        Returns:
            The sum of the number of unique answers for each group.
        """
        count = 0

        for group in self.answers:
            group = set(group['answers'])
            count += len(group)

        return count

    def count_complete_group_answers(self):
        """Counts the number of answers by every person in a group.

        Returns:
            The number of questions everyone answered.
        """
        count = 0

        for group in self.answers:
            freq = {}
            for answer in group['answers']:
                if answer in freq:
                    freq[answer] += 1
                else:
                    freq[answer] = 1

            # pylint: disable=unused-variable
            for key, value in freq.items():
                if value == group['group_size']:
                    count += 1

        return count
