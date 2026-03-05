# =========================================================
# Program Title : Contact Manager Application
# Author        : Jun Y. Ercia
#
# Description:
#     Console-based Contact Management System using
#     Object-Oriented Programming.
#
# Features:
#     - Add contact
#     - Update contact
#     - Delete contact
#     - Search contact
#     - View contacts
#     - CSV persistence
#     - Philippine phone validation
#
# Preconditions:
#     Python must be installed.
#
# Postconditions:
#     Contacts are stored in contacts.csv
# =========================================================

from contact_application import ContactApplication


# ---------------------------------------------------------
# Function: main
#
# Purpose:
#     Program entry point.
#
# Preconditions:
#     ContactApplication class must exist.
#
# Postconditions:
#     Application loop starts.
# ---------------------------------------------------------
def main():

    application = ContactApplication()
    application.run()


if __name__ == "__main__":
    main()
