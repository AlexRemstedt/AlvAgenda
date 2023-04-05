from agenda import Agenda
import os


def main():
    cwd = os.getcwd()
    print(cwd)
    Agenda.from_prompt()


if __name__ == "__main__":
    main()
