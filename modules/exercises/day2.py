from modules.helper import Helper


class Day2:
    def __init__(self, password_file):
        self.password_list = Helper.load_file(password_file)

    def count_valid_passwords_part1(self):
        correct_passwords = 0

        for password_entry in self.password_list:
            password = Password(password_entry)
            if password.validate_password_part1() is True:
                correct_passwords += 1

        return correct_passwords

    def count_valid_passwords_part2(self):
        correct_passwords = 0

        for password_entry in self.password_list:
            password = Password(password_entry)
            if password.validate_password_part2() is True:
                correct_passwords += 1

        return correct_passwords


class Password:
    def __init__(self, password_unparsed):
        password_unparsed = password_unparsed.split()
        self.lower_threshold = int(password_unparsed[0].split('-')[0])
        self.upper_threshold = int(password_unparsed[0].split('-')[1])
        self.letter = password_unparsed[1].strip(":")
        self.password = password_unparsed[2]

    def validate_password_part1(self):
        letter_count = self.password.count(self.letter)

        if (letter_count >= self.lower_threshold) and (letter_count <= self.upper_threshold):
            return True

        return False

    def validate_password_part2(self):
        if (self.letter == self.password[self.lower_threshold - 1]) is not (self.letter == self.password[self.upper_threshold - 1]):
            return True

        return False
