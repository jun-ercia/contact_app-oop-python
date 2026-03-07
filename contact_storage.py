"""
File Name: contact_storage.py
Program: Contact Manager Application

Author: Jun Y. Ercia

Description:
Provides persistent storage for contacts using a CSV file.
This class handles reading and writing contact data.
"""

import csv
from contact import Contact


class ContactStorage:

    FILE_NAME = "contacts.csv"

    def load_contacts(self):
        """Loads contacts from the CSV file."""

        contacts = []

        try:
            with open(self.FILE_NAME, newline="") as file:

                reader = csv.reader(file)

                for row in reader:

                    if len(row) == 3:
                        contacts.append(Contact(row[0], row[1], row[2]))

        except FileNotFoundError:
            pass

        return contacts

    def save_contacts(self, contacts):
        """Writes the contact list to the CSV file."""

        with open(self.FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            for contact in contacts:
                writer.writerow(contact.to_list())
