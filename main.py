import modules.exercises

# app = modules.exercises.Day1("inputs/day1/expense_report.txt")

# print("Compare two: %s" % app.expense_compare_two(2020))
# print("Compare three: %s" % app.expense_compare_three(2020))

app = modules.exercises.Day2("inputs/day2/passwords.txt")

print(app.count_valid_passwords_part1())

print(app.count_valid_passwords_part2())
