"""Advent of Code helper module.

This module contains misc, common functions for the Advent of Code project.

"""
# pylint: disable=too-few-public-methods
import sys


class Helper:
    """This class contains various common, static functions."""
    @staticmethod
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
