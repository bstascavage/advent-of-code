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

    This class loads a list of assembly instructions to check for loops

    Args:
        instruction_file (str): Path to the list of assembly instructions.

    Attributes:
        instructions (str): Post-processed array of assembly instructions.
        fixed_loop (bool): Boolean to indicate if the loop has been fixed.
            This variable is probably not needed but I am too lazy to figure out
            a better way ATM.
    """

    def __init__(self, instruction_file):
        self.instructions = []
        self.fixed_loop = False

        # This logic split this horrible file into an array of dicts.
        # Since the delemeter is "double newline" instead of a single one,
        # we need to split on "\n\n".
        for line in Helper.load_file(instruction_file):
            processed_line = line.split()
            self.instructions.append(
                {"operation": processed_line[0], "arg": int(processed_line[1])})

    def check_loop(self):
        """Checks the list of instructions for a loop.

        Returns:
            The acc value at the time the loop was discovered.
        """
        used_instructions = set()

        return self.process_instruction(self.instructions,
                                        used_instructions)

    def fix_loop(self):
        """Checks all loop possibilities where one 'nop' is replaced by a
        'jmp' and vice versa, to see if there is a valid loop.

        Returns:
            The acc value of a successful set of instructions.
        """
        # TODO: Only change an instructions if it was in the initial run.
        for index, item in enumerate(self.instructions):
            copy_instructions = copy.deepcopy(self.instructions)
            used_instructions = set()
            should_run = False
            self.fixed_loop = True

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
                    copy_instructions, used_instructions)

            if self.fixed_loop:
                return acc

        return None

    def process_instruction(self, instructions, used_instructions, index=0, acc=0):
        """Processed the assembly instructions.  This method is run recursively and
            will return the acc value, either when a loop is discovered or when
            the instructions complete.

        Args:
            instructions (list): List of instructions to run.
            used_instructions (set): A set of instructions that have already been run.
            index (int): The current instruction location.
            acc (int): The current acc value.
        Returns:
            The acc value after the instruction is run.
        """
        instruction = instructions[index]

        if index in used_instructions:
            self.fixed_loop = False
            return acc
        used_instructions.add(index)

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
                instructions, used_instructions, acc=acc, index=index)

        return acc
