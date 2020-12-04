"""Advent of Code Day 4 module.

This module is used to solved Day 4's problem for the Advent of Code.
You can find the problem here:

https://adventofcode.com/2020/day/1

"""
# pylint: disable=import-error, too-few-public-methods
from modules.helper import Helper

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
optional_fields = {"cid"}


class Day4:
    """This class is an object for the Day 4 problem.

    This class loads an passport list file and does various verifications.

    Args:
        passport_file (str): Path to the passport list file.

    Attributes:
        passport_list (str): Post-processed list of passport entries dicts.

    """

    def __init__(self, passport_file):
        self.passport_list = []

        # This logic split this horrible file into an array of dicts.
        # Since the delemeter is "double newline" instead of a single one,
        # we need to split on "\n\n".  We also have to do some fancy string manpulation
        # because the file isn't quite in dict format.
        for line in Helper.load_file(passport_file, "\n\n"):
            line = line.replace("\n", " ")
            self.passport_list.append({i.split(':')[0]: i.split(':')[1]
                                       for i in line.split(' ')})

    def count_valid_passports(self, optional=False):
        """Loops through a list of passport entries, checking to see if a passport
            contains all the required fields.

        Args:
            optional (bool): If set to True, also check optional passport fields.
        Returns:
            The total number of valid passowrds.
        """
        valid_passports = 0

        for passport in self.passport_list:
            if not optional:
                if (passport.keys()) >= required_fields:
                    valid_passports += 1
            else:
                all_fields = required_fields.union(optional_fields)
                if (passport.keys()) >= all_fields:
                    valid_passports += 1

        return valid_passports
