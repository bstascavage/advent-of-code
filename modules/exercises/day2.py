"""Advent of Code Day 2 module.

This module is used to solved Day 2's problem for the Advent of Code.
You can find the problem here:

https://adventofcode.com/2020/day/2

"""
# pylint: disable=import-error,no-name-in-module
from modules.helper import Helper


class Day2:
    """This class is an object for the Day 2 problem.

    This class loads a password file and does various validation functions.
    Each line in the password file has the following format:
    <lower_threshold>-<upper_threshold> <letter_to_verify>: <password>

    Args:
        password_file (str): Path to the password file.

    Attributes:
        password_list (str): List of passwords.

    """

    def __init__(self, password_file):
        self.password_list = Helper.load_file(password_file)

    def count_valid_passwords_part1(self):
        """Loops through a list of passwords, checking to see if the number of instances of `letter`
        is greater than `lower_threshold` and lower than `upper_theshold`.

        Returns:
            The number of passwords that meet their password requirements (int).
        """
        correct_passwords = 0

        for password_entry in self.password_list:
            password = Password(password_entry)
            if password.validate_password_part1() is True:
                correct_passwords += 1

        return correct_passwords

    def count_valid_passwords_part2(self):
        """Loops through a list of passwords, checking to see if an instance of `letter`
        is defined in one of two positions in the password string, where the indices are
        `lower_threshold` and `upper_threshold`.

        Returns:
            The number of passwords that meet their password requirements (int).
        """
        correct_passwords = 0

        for password_entry in self.password_list:
            password = Password(password_entry)
            if password.validate_password_part2() is True:
                correct_passwords += 1

        return correct_passwords


class Password:
    """This class is a Password object for the Day 2 problem.

    This class defined a password object based on the Day 2 password format,
    and does various validation functions. The purpose `upper_threshold` and `lower_threshold`
    varies depending on the function.

    Args:
        password (str): Password value.
        lower_threshold (int): Lower-bound value for verification.
        upper_threshold (int): Upper-bound value for verification.
        letter (str): Specific character to use for various verification.

    Attributes:
        password_list (str): List of passwords.

    """

    def __init__(self, password_unparsed):
        password_unparsed = password_unparsed.split()
        self.lower_threshold = int(password_unparsed[0].split('-')[0])
        self.upper_threshold = int(password_unparsed[0].split('-')[1])
        self.letter = password_unparsed[1].strip(":")
        self.password = password_unparsed[2]

    def validate_password_part1(self):
        """Validates a password, checking to see if the number of instances of `letter`
        is greater than `lower_threshold` and lower than `upper_theshold`.

        Returns:
            True if password is valid, False otherwise.
        """
        letter_count = self.password.count(self.letter)

        if self.lower_threshold <= letter_count <= self.upper_threshold:
            return True

        return False

    def validate_password_part2(self):
        """Validates a password, checking to see if an instance of `letter`
        is defined in one of two positions in the password string, where the indices are
        `lower_threshold` and `upper_threshold`

        Returns:
            True if password is valid, False otherwise.
        """
        # pylint: disable=superfluous-parens
        if (self.letter == self.password[self.lower_threshold - 1]) is not \
                (self.letter == self.password[self.upper_threshold - 1]):
            return True

        return False
