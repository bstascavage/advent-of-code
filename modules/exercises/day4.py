"""Advent of Code Day 4 module.

This module is used to solved Day 4's problem for the Advent of Code.
You can find the problem here:

https://adventofcode.com/2020/day/1

"""
# pylint: disable=import-error, too-few-public-methods
from modules.helper import Helper
import re


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

            passport = Passport({i.split(':')[0]: i.split(':')[
                                1] for i in line.split(' ')})
            if passport.has_required_fields:
                self.passport_list.append(passport)

    def count_valid_passports(self, optional=False):
        """Loops through a list of passport entries, checking to see if a passport
            contains all the required fields.

        Args:
            optional (bool): If set to True, also check optional passport fields.
        Returns:
            The total number of valid passowrds.
        """
        if optional:
            valid_passports = 0
            for passport in self.passport_list:
                if passport.has_all_fields:
                    valid_passports += 1

            return valid_passports

        return len(self.passport_list)

    def count_valid_passports_strict(self, optional=False):
        valid_passports = 0

        for passport in self.passport_list:
            if passport.verify_fields_strict():
                valid_passports += 1
            print("*********************")
        return valid_passports


class Passport:
    year_length = 4
    birth_year_lower = 1920
    birth_year_upper = 2002

    issue_year_lower = 2010
    issue_year_upper = 2020

    expired_year_lower = 2020
    expired_year_upper = 2030

    height_lower = {"cm": 150, "in": 59}
    height_upper = {"cm": 193, "in": 76}

    eye_color_lookup = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    optional_fields = {"cid"}
    all_fields = required_fields.union(optional_fields)

    # Defaults
    has_all_fields = False
    has_required_fields = False
    has_optional_fields = False

    def parse_height(self, height_string):
        match = re.compile("[^\W\d]").search(height_string)
        if bool(match):
            return {"value": int(height_string[:match.start()]), "unit": height_string[match.start():]}

        return None

    def __init__(self, passport_raw):
        self.passport_raw = passport_raw

        if (passport_raw.keys()) >= self.all_fields:
            self.has_all_fields = True
            self.has_optional_fields = True
            self.has_required_fields = True
        if (passport_raw.keys()) >= self.required_fields:
            self.has_required_fields = True

        if self.has_required_fields:
            self.birth_year = int(passport_raw["byr"])
            self.issue_year = int(passport_raw["iyr"])
            self.expired_year = int(passport_raw["eyr"])

            self.height = self.parse_height(passport_raw["hgt"])

            self.hair_color = passport_raw["hcl"]
            self.eye_color = passport_raw["ecl"]
            self.passport_id = passport_raw["pid"]

            if "cid" in passport_raw:
                self.country_id = passport_raw["cid"]

    def verify_birth(self):
        if len(str(self.birth_year)) == self.year_length and (self.birth_year_lower <= self.birth_year <= self.birth_year_upper):
            return True
        else:
            return False

    def verify_issue(self):
        if len(str(self.issue_year)) == self.year_length and (self.issue_year_lower <= self.issue_year <= self.issue_year_upper):
            return True
        else:
            return False

    def verify_expired(self):
        if len(str(self.expired_year)) == self.year_length and (self.expired_year_lower <= self.expired_year <= self.expired_year_upper):
            return True
        else:
            return False

    def verify_height(self):
        if self.height is not None:
            if self.height_lower[self.height["unit"]] <= self.height["value"] <= self.height_upper[self.height["unit"]]:
                return True

        return False

    def verify_hair_color(self):
        if self.hair_color.startswith("#") and (len(self.hair_color) == 7):
            try:
                int(self.hair_color.strip("#"), 16)
                return True
            except ValueError:
                return False

        return False

    def verify_eye_color(self):
        print("Eyecolor: %s" % self.eye_color)

        if self.eye_color in self.eye_color_lookup:
            return True

        return False

    def verify_passport_id(self):
        if len(self.passport_id) == 9 and self.passport_id.isdigit():
            print("PID: %s" % self.passport_id.isdigit())
            return True

        return False

    def verify_fields_strict(self):
        if self.verify_birth() and self.verify_issue() and self.verify_expired() and self.verify_height() and self.verify_hair_color() and self.verify_eye_color() and self.verify_passport_id():
            print(self.passport_raw)
            return True
