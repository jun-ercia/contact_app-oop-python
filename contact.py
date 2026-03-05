from person import Person


# =========================================================
# Class: Contact
#
# Description:
#     Represents a contact with phone and email.
# =========================================================


class Contact(Person):

    # -----------------------------------------------------
    # Constructor
    #
    # Preconditions:
    #     name, phone, email must be strings
    #
    # Postconditions:
    #     Contact object created
    # -----------------------------------------------------
    def __init__(self, name, phone_number, email):

        super().__init__(name)
        self.__phone_number = phone_number
        self.__email = email

    # -----------------------------------------------------
    # Function: get_phone_number
    #
    # Postconditions:
    #     Returns phone number
    # -----------------------------------------------------
    def get_phone_number(self):

        return self.__phone_number

    # -----------------------------------------------------
    # Function: get_email
    #
    # Postconditions:
    #     Returns email address
    # -----------------------------------------------------
    def get_email(self):

        return self.__email

    # -----------------------------------------------------
    # Function: set_phone_number
    #
    # Postconditions:
    #     Updates phone number
    # -----------------------------------------------------
    def set_phone_number(self, phone):

        self.__phone_number = phone

    # -----------------------------------------------------
    # Function: set_email
    #
    # Postconditions:
    #     Updates email address
    # -----------------------------------------------------
    def set_email(self, email):

        self.__email = email

    # -----------------------------------------------------
    # Function: to_list
    #
    # Postconditions:
    #     Returns contact data as list
    # -----------------------------------------------------
    def to_list(self):

        return [self.get_name(), self.__phone_number, self.__email]

    # -----------------------------------------------------
    # Function: display
    #
    # Postconditions:
    #     Displays contact information
    # -----------------------------------------------------
    def display(self):

        super().display()
        print(f"Phone : {self.__phone_number}")
        print(f"Email : {self.__email}")
