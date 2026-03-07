"""
File Name: contact_manager.py
Program: Contact Manager Application

Author: Jun Y. Ercia

Description:
Implements the ContactManager class responsible for managing
all contact-related operations including creation, updating,
deletion, searching, and displaying contacts.

The class also validates phone numbers and coordinates
persistent storage through the ContactStorage component.
"""

import re
from contact_storage import ContactStorage


class ContactManager:

    def __init__(self):
        """Initializes the storage system and loads existing contacts."""

        self.__storage = ContactStorage()
        self.__contacts = self.__storage.load_contacts()

    def validate_phone(self, phone):
        """
        Validates Philippine mobile phone numbers.

        Format:
            09XXXXXXXXX
        """
        pattern = r"^09\d{9}$"
        return re.match(pattern, phone)

    def add_contact(self, contact):
        """Adds a new contact and saves the updated list."""

        if not self.validate_phone(contact.get_phone_number()):
            print("Invalid Philippine phone number.")
            return

        self.__contacts.append(contact)
        self.__storage.save_contacts(self.__contacts)

        print("Contact added.")

    def view_contacts(self):
        """Displays all stored contacts."""

        if not self.__contacts:
            print("No contacts.")
            return

        for contact in self.__contacts:
            print("----------------")
            contact.display()

    def search_contact(self, keyword):
        """
        Searches contacts by name, phone number, or email.
        Returns a list of matching contacts.
        """

        results = []

        for contact in self.__contacts:

            if (
                keyword.lower() in contact.get_name().lower()
                or keyword in contact.get_phone_number()
                or keyword.lower() in contact.get_email().lower()
            ):
                results.append(contact)

        return results

    def update_contact(self, name):
        """Updates an existing contact's phone number and email."""

        for contact in self.__contacts:

            if contact.get_name().lower() == name.lower():

                new_phone = input("New phone: ")
                new_email = input("New email: ")

                if not self.validate_phone(new_phone):
                    print("Invalid phone.")
                    return

                contact.set_phone_number(new_phone)
                contact.set_email(new_email)

                self.__storage.save_contacts(self.__contacts)

                print("Contact updated.")
                return

        print("Contact not found.")

    def delete_contact(self, name):
        """Deletes a contact from the list."""

        for contact in self.__contacts:

            if contact.get_name().lower() == name.lower():

                self.__contacts.remove(contact)
                self.__storage.save_contacts(self.__contacts)

                print("Contact deleted.")
                return

        print("Contact not found.")
