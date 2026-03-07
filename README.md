# Contact Manager Application (Python)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-Educational-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

A console-based **Contact Management System** implemented in **Python** using **Object-Oriented Programming (OOP)** principles and modular architecture.

This application allows users to manage personal contact records through a **menu-driven command-line interface** while storing data persistently using a **CSV file**.

# Features

* Add new contacts
* Update existing contacts
* Delete contacts
* Search contacts by name, phone number, or email
* View all contacts
* Philippine phone number validation (`09XXXXXXXXX`)
* CSV-based data storage
* Menu-driven command-line interface
* Modular object-oriented design


# System Architecture

The application follows a simple layered architecture separating the user interface, application logic, and data storage.

```
User
  │
  ▼
ContactApplication
  │
  ▼
ContactManager
  │
  ▼
ContactStorage
  │
  ▼
contacts.csv
```


# Object-Oriented Design

The system is implemented using several classes with clear responsibilities.

| Class              | Responsibility                                 |
| ------------------ | ---------------------------------------------- |
| ContactApplication | Controls the main program flow                 |
| Menu               | Displays menu options and validates user input |
| ContactManager     | Handles contact operations (CRUD)              |
| ContactStorage     | Manages CSV file storage                       |
| Contact            | Represents a contact record                    |
| Person             | Base class containing a name                   |


# Project Structure

```
contact-manager-python/
│
├── main.py
├── contact_application.py
├── contact_manager.py
├── contact_storage.py
├── contact.py
├── person.py
├── menu.py
│
├── contacts.csv
└── README.md
```

# Requirements

* Python 3.x

The program uses only **Python standard libraries**, so no external packages are required.


# Installation

Clone the repository:

```
git clone https://github.com/yourusername/contact-manager-python.git
```

Navigate to the project directory:

```
cd contact-manager-python
```

Run the application:

```
python main.py
```

---

# Example Menu

```
====== MENU ======
[1] Add Contact
[2] Update Contact
[3] Delete Contact
[4] Search Contact
[5] View Contacts
[6] Exit
==================
```

---

# Phone Number Validation

The system validates Philippine mobile numbers using the following format:

```
09XXXXXXXXX
```

Example:

```
09123456789
```

Validation pattern used:

```
^09\d{9}$
```

---

# Sample Contact Record

Example CSV data stored in `contacts.csv`:

```
Juan Cruz,09123456789,juan@email.com
Maria Santos,09987654321,maria@email.com
```

# Future Improvements

Potential enhancements for future versions include:

* Graphical User Interface (GUI)
* SQLite or MySQL database integration
* Contact grouping or categorization
* Import and export functionality
* Mobile or web-based version


# Contributing

Contributions are welcome. You may:

1. Fork the repository
2. Create a new branch
3. Submit a pull request with improvements


# Author

Jun Y. Ercia

# License

This project is provided for **educational purposes**.
You may modify and reuse the code with proper attribution.

