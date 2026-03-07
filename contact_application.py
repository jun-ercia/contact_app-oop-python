"""
File Name: contact_application.py
Program: Contact Manager Application

Author: Jun Y. Ercia

Description:
Defines the ContactApplication class which acts as the main
controller of the system. It coordinates the interaction
between the user interface (Menu) and the contact management
logic (ContactManager).
"""

from contact import Contact
from contact_manager import ContactManager
from menu import Menu


class ContactApplication:

    def __init__(self):
        """Initializes the menu and contact manager."""

        self.__menu = Menu([
            "Add Contact",
            "Update Contact",
            "Delete Contact",
            "Search Contact",
            "View Contacts",
            "Exit"
        ])

        self.__manager = ContactManager()

    def run(self):
        """
        Executes the main program loop.

        The system repeatedly displays the menu and performs
        the selected operation until the user exits.
        """

        while True:

            option = self.__menu.display()

            if option == 1:
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")

                contact = Contact(name, phone, email)
                self.__manager.add_contact(contact)

            elif option == 2:
                name = input("Contact to update: ")
                self.__manager.update_contact(name)

            elif option == 3:
                name = input("Contact to delete: ")
                self.__manager.delete_contact(name)

            elif option == 4:
                keyword = input("Search keyword: ")
                results = self.__manager.search_contact(keyword)

                for contact in results:
                    print("----------------")
                    contact.display()

            elif option == 5:
                self.__manager.view_contacts()

            elif option == 6:
                print("Goodbye.")
                break
