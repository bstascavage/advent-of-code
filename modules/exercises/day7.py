"""Advent of Code Day 7 module.

This module is used to solved Day 7's problem for the Advent of Code.
You can find the problem here:

https://adventofcode.com/2020/day/7

"""
# pylint: disable=import-error
import re
from modules.helper import Helper


class Day7:
    """This class is an object for the Day 7 problem.

    This class loads a list of baggage rules and creates a tree of all dependencies.

    Args:
        baggage_file (str): Path to the baggage rules file.

    Attributes:
        rules_count_unique (dict): Dict of rules to transverse to count number of
            unique bags from source bag.
        rules_count_all (dict): Dict of rules to transverse to count total number of
            bags from source bag.
    """

    def __init__(self, baggage_file):
        self.rules_count_unique = {}
        self.rules_count_all = {}
        preprocessed_rules = Helper.load_file(baggage_file)

        # Loading dict for part 1.
        # Format: {bag1: [bag2, bag3], bag2: [bag3, bag4]}
        for rule in preprocessed_rules:

            rule = re.sub(r'(?:bag(s)?(\s)?(\.)?|\d+\s)', '', rule)
            rule = re.sub(r'\s(?:contain|,)\s', "-", rule).strip().split('-')

            bag_key = rule.pop(0)
            for item in rule:
                if item not in self.rules_count_unique:
                    self.rules_count_unique[item] = []
                self.rules_count_unique[item].append(bag_key)

        # Loading dict for part 2.
        # Format: {bag1: [{unit: bag2, quanity: 1}, {unit: bag3, quanity: 3}], \
        #   bag2: [{unit: bag4, quanity: 1}]}
        for rule in preprocessed_rules:
            rule = re.sub(r'bag(s)?(\s)?(\.)?', '', rule)
            rule = re.sub(r'\s(?:contain|,)\s', "-", rule).strip().split('-')

            bag_key = rule.pop(0)
            if bag_key not in self.rules_count_all:
                self.rules_count_all[bag_key] = []
            for item in rule:
                items = item.split(" ", 1)
                if items[0] == "no":
                    break
                self.rules_count_all[bag_key].append(
                    {"quanity": int(items[0]), "unit": items[1]})

    def count_paths_to_bag(self, bag, bag_list):

        if bag in self.rules_count_unique:
            for bags in self.rules_count_unique[bag]:
                if bags not in bag_list:
                    bag_list.add(bags)
                    bag_list = self.count_paths_to_bag(bags, bag_list)

        return bag_list

    def get_bag_count(self, bag):
        unique_bags = set()

        self.count_paths_to_bag(bag, unique_bags)

        return len(unique_bags)

    def get_nested_bags(self, bag, count=0):
        if not self.rules_count_all[bag]:
            return 0
        for items in self.rules_count_all[bag]:
            nested_quanity = self.get_nested_bags(items["unit"])
            count += items["quanity"]*nested_quanity + items["quanity"]

        return count
