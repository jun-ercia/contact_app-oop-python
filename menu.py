# =========================================================
# Class: Menu
#
# Description:
#     Displays menu options and validates input.
# =========================================================


class Menu:

    def __init__(self, options):

        self.__options = options

    def display(self):

        print("\n====== MENU ======")

        for i, option in enumerate(self.__options, start=1):
            print(f"[{i}] {option}")

        print("==================")

        return self.get_choice(len(self.__options))

    def get_choice(self, count):

        while True:

            try:

                choice = int(input("Enter choice: "))

                if choice not in range(1, count + 1):
                    raise ValueError

                return choice

            except ValueError:
                print("Invalid choice.")
