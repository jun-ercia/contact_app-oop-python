"""
File Name: main.py
Program: Contact Manager Application

Author: Jun Y. Ercia
Date Written: March 2026

Description:
Entry point of the Contact Manager application. This file
initializes the main application controller and starts the
program execution.

The application logic is handled by the ContactApplication
class and its related components.
"""

from contact_application import ContactApplication


def main():
    """
    Starts the Contact Manager application.

    Preconditions:
        ContactApplication class must be available.

    Postconditions:
        The application runs until the user selects the exit option.
    """

    application = ContactApplication()
    application.run()


if __name__ == "__main__":
    main()
