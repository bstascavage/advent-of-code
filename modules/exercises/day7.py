"""Advent of Code Day 7 module.

This module is used to solved Day 7's problem for the Advent of Code.
You can find the problem here:

https://adventofcode.com/2020/day/7

"""
# pylint: disable=import-error
from modules.helper import Helper
import re


class Day7:
    """This class is an object for the Day 7 problem.

    This class loads a list of baggage rules and creates a tree of all dependencies.

    Args:
        baggage_file (str): Path to the baggage rules file.

    Attributes:
        answers (str): Post-processed 2D array of questionaire answers.

    """

    def __init__(self, baggage_file):
        self.rules = {}
        self.rules_second = {}
        preprocessed_rules = Helper.load_file(baggage_file)

        for rule in preprocessed_rules:
            rule1 = re.sub(r'(?:bag(s)?(\s)?(\.)?|\d+\s)', '', rule)
            test1 = re.sub(r'\s(?:contain|,)\s', "-", rule1).strip().split('-')
            rule2 = re.sub(r'bag(s)?(\s)?(\.)?', '', rule)
            test2 = re.sub(r'\s(?:contain|,)\s', "-", rule2).strip().split('-')

            first = test1.pop(0)
            for item in test1:
                if item not in self.rules:
                    self.rules[item] = []
                self.rules[item].append(first)

            first2 = test2.pop(0)
            if first2 not in self.rules_second:
                self.rules_second[first] = []
            for item in test2:
                items = item.split(" ", 1)
                if items[0] == "no":
                    break
                self.rules_second[first].append(
                    {"quanity": int(items[0]), "unit": items[1]})

    def count_paths_to_bag(self, bag, bag_list):

        if bag in self.rules:
            for bags in self.rules[bag]:
                if bags not in bag_list:
                    bag_list.add(bags)
                    bag_list = self.count_paths_to_bag(bags, bag_list)

        return bag_list

    def get_bag_count(self, bag):
        unique_bags = set()

        self.count_paths_to_bag(bag, unique_bags)

        return len(unique_bags)

    def get_nested_bags(self, bag, count=0):
        if not self.rules_second[bag]:
            return 0
        for items in self.rules_second[bag]:
            nested_quanity = self.get_nested_bags(items["unit"])
            count += items["quanity"]*nested_quanity + items["quanity"]

        return count
