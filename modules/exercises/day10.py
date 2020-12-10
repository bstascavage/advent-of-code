"""Advent of Code Day 10 module.

This module is used to solved Day 10's problem for the Advent of Code.
You can find the problem here:

https://adventofcode.com/2020/day/10

"""
# pylint: disable=import-error, no-name-in-module
from collections import Counter
from modules.helper import Helper


class Day10:
    """This class is an object for the Day 10 problem.

    This class loads a list of integers as part of its fictional XMAS cypher protocol.

    Args:
        xmas_file (str): Path to the list of XMAS integers.

    Attributes:
        xmas_data (str): Array of XMAS integers.

    """

    def __init__(self, adapter_file):
        self.adapter_list = []
        self.adapter_list = Helper.load_file(adapter_file, cast_int=True)
        self.adapter_list.append(0)
        self.adapter_list.sort()

    def find_freq(self):
        start = 0
        jolt_counter = Counter({3: 1})

        for item in self.adapter_list:
            if item != 0:
                jolt_counter[item-start] += 1
            start = item

        return jolt_counter[1]*jolt_counter[3]

    def find_path(self):
        jolt_counter = Counter({0: 1})

        for x in self.adapter_list:
            jolt_counter[x+1] += jolt_counter[x]
            jolt_counter[x+2] += jolt_counter[x]
            jolt_counter[x+3] += jolt_counter[x]

        return jolt_counter[max(self.adapter_list) + 3]
