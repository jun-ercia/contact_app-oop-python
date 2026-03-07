"""
File Name: menu.py
Program: Contact Manager Application

Author: Jun Y. Ercia

Description:
Implements a simple menu interface that displays options
and validates user input.
"""


class Menu:

    def __init__(self, options):
        """Initializes menu options."""
        self.__options = options

    def display(self):
        """Displays menu options and returns user selection."""

        print("\n====== MENU ======")

        for i, option in enumerate(self.__options, start=1):
            print(f"[{i}] {option}")

        print("==================")

        return self.get_choice(len(self.__options))

    def get_choice(self, count):
        """Validates the user's menu choice."""

        while True:

            try:
                choice = int(input("Enter choice: "))

                if choice not in range(1, count + 1):
                    raise ValueError

                return choice

            except ValueError:
                print("Invalid choice.")
