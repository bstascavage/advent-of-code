EXPENSE_REPORT = "expense_report.txt"


def main():
    expense_list = load_file(EXPENSE_REPORT)

    # Ensuring that every element in the list is set as an int
    expense_list = [int(i) for i in expense_list]

    print(expense_compare(expense_list))


def load_file(file):
    input_file = open(file, "r")
    output_list = input_file.read().split("\n")
    input_file.close()
    return output_list


def expense_compare(list):
    list.sort()

    for first_entry in list:
        for second_entry in list:
            if (first_entry + second_entry) == 2020:
                return first_entry * second_entry


if __name__ == "__main__":
    main()
