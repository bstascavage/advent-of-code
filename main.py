EXPENSE_REPORT = "expense_report.txt"


def main():
    report = open(EXPENSE_REPORT, "r")
    expense_list = report.read().split("\n")
    report.close()
    expense_list = [int(i) for i in expense_list]

    print(expense_compare(expense_list))


def expense_compare(expense_list):
    expense_list.sort()

    for first_entry in expense_list:
        for second_entry in expense_list:
            if (first_entry + second_entry) == 2020:
                return first_entry * second_entry


if __name__ == "__main__":
    main()
