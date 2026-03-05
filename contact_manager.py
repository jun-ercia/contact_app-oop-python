import csv
import re
from contact import Contact


# =========================================================
# Class: ContactManager
#
# Description:
#     Manages contact operations and CSV storage.
# =========================================================


class ContactManager:

    FILE_NAME = "contacts.csv"

    # -----------------------------------------------------
    # Constructor
    #
    # Postconditions:
    #     Contact list initialized and data loaded
    # -----------------------------------------------------
    def __init__(self):

        self.__contacts = []
        self.load_contacts()

    # -----------------------------------------------------
    # Function: validate_phone
    #
    # Purpose:
    #     Validate Philippine mobile number
    #
    # Format:
    #     09XXXXXXXXX
    # -----------------------------------------------------
    def validate_phone(self, phone):

        pattern = r"^09\d{9}$"
        return re.match(pattern, phone)

    # -----------------------------------------------------
    # Function: load_contacts
    #
    # Postconditions:
    #     Contacts loaded from CSV
    # -----------------------------------------------------
    def load_contacts(self):

        try:

            with open(self.FILE_NAME, newline="") as file:

                reader = csv.reader(file)

                for row in reader:

                    if len(row) == 3:
                        contact = Contact(row[0], row[1], row[2])
                        self.__contacts.append(contact)

        except FileNotFoundError:
            pass

    # -----------------------------------------------------
    # Function: save_contacts
    #
    # Postconditions:
    #     Contact list saved to CSV
    # -----------------------------------------------------
    def save_contacts(self):

        with open(self.FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            for contact in self.__contacts:
                writer.writerow(contact.to_list())

    # -----------------------------------------------------
    # Function: add_contact
    # -----------------------------------------------------
    def add_contact(self, contact):

        if not self.validate_phone(contact.get_phone_number()):
            print("Invalid Philippine phone number.")
            return

        self.__contacts.append(contact)
        self.save_contacts()

        print("Contact added.")

    # -----------------------------------------------------
    # Function: view_contacts
    # -----------------------------------------------------
    def view_contacts(self):

        if not self.__contacts:
            print("No contacts.")
            return

        for contact in self.__contacts:
            print("----------------")
            contact.display()

    # -----------------------------------------------------
    # Function: search_contact
    # -----------------------------------------------------
    def search_contact(self, keyword):

        results = []

        for contact in self.__contacts:

            if (
                keyword.lower() in contact.get_name().lower()
                or keyword in contact.get_phone_number()
                or keyword.lower() in contact.get_email().lower()
            ):
                results.append(contact)

        return results

    # -----------------------------------------------------
    # Function: update_contact
    # -----------------------------------------------------
    def update_contact(self, name):

        for contact in self.__contacts:

            if contact.get_name().lower() == name.lower():

                new_phone = input("New phone: ")
                new_email = input("New email: ")

                if not self.validate_phone(new_phone):
                    print("Invalid phone.")
                    return

                contact.set_phone_number(new_phone)
                contact.set_email(new_email)

                self.save_contacts()

                print("Contact updated.")
                return

        print("Contact not found.")

    # -----------------------------------------------------
    # Function: delete_contact
    # -----------------------------------------------------
    def delete_contact(self, name):

        for contact in self.__contacts:

            if contact.get_name().lower() == name.lower():

                self.__contacts.remove(contact)
                self.save_contacts()

                print("Contact deleted.")
                return

        print("Contact not found.")
