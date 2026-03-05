# =========================================================
# Class: Person
#
# Description:
#     Represents a person entity containing a name.
# =========================================================


class Person:

    # -----------------------------------------------------
    # Constructor
    #
    # Preconditions:
    #     name must be string
    #
    # Postconditions:
    #     Person object created
    # -----------------------------------------------------
    def __init__(self, name):

        self.__name = name

    # -----------------------------------------------------
    # Function: get_name
    #
    # Postconditions:
    #     Returns stored name
    # -----------------------------------------------------
    def get_name(self):

        return self.__name

    # -----------------------------------------------------
    # Function: set_name
    #
    # Postconditions:
    #     Updates stored name
    # -----------------------------------------------------
    def set_name(self, name):

        self.__name = name

    # -----------------------------------------------------
    # Function: display
    #
    # Postconditions:
    #     Prints person's name
    # -----------------------------------------------------
    def display(self):

        print(f"Name : {self.__name}")
