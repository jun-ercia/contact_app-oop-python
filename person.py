"""
File Name: person.py
Program: Contact Manager Application

Author: Jun Y. Ercia

Description:
Defines the Person class which stores a person's name and
serves as the base class for Contact.
"""


class Person:

    def __init__(self, name):
        """Initializes a person with a name."""
        self.__name = name

    def get_name(self):
        """Returns the person's name."""
        return self.__name

    def set_name(self, name):
        """Updates the person's name."""
        self.__name = name

    def display(self):
        """Displays the person's name."""
        print(f"Name : {self.__name}")
