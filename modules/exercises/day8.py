"""Advent of Code Day 8 module.

This module is used to solved Day 6's problem for the Advent of Code.
You can find the problem here:

https://adventofcode.com/2020/day/6

"""
# pylint: disable=import-error
import copy
from modules.helper import Helper


class Day8:
    """This class is an object for the Day 8 problem.

    This class loads a list of questionaire form answer from a file
    and does various search functions.

    Args:
        form_file (str): Path to the list of questionaire form answer file.

    Attributes:
        answers (str): Post-processed 2D array of questionaire answers.

    """

    def __init__(self, form_file):
        self.instructions = []
        self.acc_global = 0
        self.commands = set()
        self.test_bool = False

        # This logic split this horrible file into an array of dicts.
        # Since the delemeter is "double newline" instead of a single one,
        # we need to split on "\n\n".
        for line in Helper.load_file(form_file):
            processed_line = line.split()
            self.instructions.append(
                {"operation": processed_line[0], "arg": int(processed_line[1])})

    def check_loop(self, fix=False):
        used_commands = set()

        self.acc_global = self.process_instruction(self.instructions,
                                                   0, 0, used_commands)

        return self.acc_global

    def check_all_loops(self):

        # TODO: Only change an instructions if it was in the initial run.
        for index, item in enumerate(self.instructions):
            copy_instructions = copy.deepcopy(self.instructions)
            used_commands = set()
            should_run = False
            self.test_bool = True

            if item['operation'] == "jmp":
                copy_instructions[index]['operation'] = "nop"
                should_run = True

            elif item['operation'] == "nop":
                copy_instructions[index]['operation'] = "jmp"
                should_run = True
            else:
                continue
            if should_run:
                acc = self.process_instruction(
                    copy_instructions, 0, 0, used_commands)

            if self.test_bool:
                return acc

        return None

    def process_instruction(self, instructions, index, acc, used_commands):
        instruction = instructions[index]

        if index in used_commands:
            self.test_bool = False
            return acc
        used_commands.add(index)

        if instruction["operation"] == "acc":
            acc += instruction["arg"]
        if instruction["operation"] == "nop":
            pass

        if instruction["operation"] == "jmp":
            index += instruction["arg"]
        else:
            index += 1

        if index <= len(self.instructions) - 1:
            acc = self.process_instruction(
                instructions, index, acc, used_commands)

        return acc
