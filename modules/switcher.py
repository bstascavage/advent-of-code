import importlib


class Switcher(object):
    def __init__(self, exercise_name):
        module = importlib.import_module('.exercises', package='modules')
        exercise_class = getattr(module, exercise_name)
        self.exercise_app = exercise_class(
            "inputs/%s/input.txt" % exercise_name.lower())
        self.exercise_name = exercise_name

    def run_exercise(self):
        function = getattr(self, self.exercise_name.lower(),
                           lambda: "Invalid function")
        return function()

    def print_results(self, answer_one, answer_two):
        print("********%s*******" % self.exercise_name)
        print("Part 1: %s" % answer_one)
        print("Part 2: %s" % answer_two)
        print("*******************")

    def day1(self):
        part_one_answer = self.exercise_app.expense_compare_two(2020)
        part_two_answer = self.exercise_app.expense_compare_three(2020)

        self.print_results(part_one_answer, part_two_answer)

    def day2(self):
        part_one_answer = self.exercise_app.count_valid_passwords_part1()
        part_two_answer = self.exercise_app.count_valid_passwords_part2()

        self.print_results(part_one_answer, part_two_answer)

    def day3(self):
        part_one_answer = self.exercise_app.find_trees_in_path(3, 1)
        part_two_answer = self.exercise_app.find_trees_in_path(1, 1) * self.exercise_app.find_trees_in_path(
            3, 1) * self.exercise_app.find_trees_in_path(5, 1) * self.exercise_app.find_trees_in_path(7, 1) * self.exercise_app.find_trees_in_path(1, 2)

        self.print_results(part_one_answer, part_two_answer)
