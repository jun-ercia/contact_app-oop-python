"""
File Name: contact.py
Program: Contact Manager Application

Author: Jun Y. Ercia

Description:
Defines the Contact class representing a contact record
containing name, phone number, and email address.
"""

from person import Person


class Contact(Person):

    def __init__(self, name, phone_number, email):
        """Creates a contact with phone number and email."""

        super().__init__(name)

        self.__phone_number = phone_number
        self.__email = email

    def get_phone_number(self):
        """Returns the phone number."""
        return self.__phone_number

    def get_email(self):
        """Returns the email address."""
        return self.__email

    def set_phone_number(self, phone):
        """Updates the phone number."""
        self.__phone_number = phone

    def set_email(self, email):
        """Updates the email address."""
        self.__email = email

    def to_list(self):
        """Converts contact data into a list for CSV storage."""
        return [self.get_name(), self.__phone_number, self.__email]

    def display(self):
        """Displays contact information."""

        super().display()
        print(f"Phone : {self.__phone_number}")
        print(f"Email : {self.__email}")
