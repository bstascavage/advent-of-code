import os
from dotenv import load_dotenv
from modules.switcher import Switcher

load_dotenv()


def main():
    s = Switcher(os.getenv("ADVENT_DAY"))
    s.run_exercise()


if __name__ == "__main__":
    main()
