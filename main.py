"""Advent of Code main module.

This module is used to determine which 'day' module to use, and is the
top-level module to run for these exercises.  For more information:

https://adventofcode.com/2020/

"""
import os

# pylint: disable=import-error,no-name-in-module
from dotenv import load_dotenv
from modules.switcher import Switcher

load_dotenv()


def main():
    """Main function for the Advent of Code project.

    """
    day = Switcher(os.getenv("ADVENT_DAY"))
    day.run_exercise()


if __name__ == "__main__":
    main()
