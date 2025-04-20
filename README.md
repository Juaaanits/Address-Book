# Address Book Management System

## Overview
This is a console-based Address Book Management System built using Python. It allows users to manage their contacts by adding, editing, deleting, viewing, and searching for contacts. The system stores contact information such as first name, last name, address, and phone number. It provides a simple and interactive menu for users to perform operations on the address book.

## Project Features
- **Add a Contact**: Allows the user to add a new contact with first name, last name, address, and phone number.
- **Edit a Contact**: Provides the option to edit the contact's full name, address, or phone number.
- **Delete a Contact**: Allows the user to delete a contact based on name and contact number.
- **View All Contacts**: Displays a list of all contacts stored in the address book.
- **Search for a Contact**: Users can search for a contact by full name or phone number.

## Requirements
- Python 3.x
- A terminal or command prompt to run the script

## Features in Detail

### 1. **Add a Contact**
Users are prompted to input:
- First name
- Last name
- Address
- Phone number

These details are validated, and the contact is added to the address book.

### 2. **Edit a Contact**
Users can modify:
- Full Name
- Address
- Phone Number

The program ensures the correct contact is found and updated.

### 3. **Delete a Contact**
Users can delete a contact by entering both the full name and contact number. The system checks that the name and number match a valid contact before deleting it.

### 4. **View All Contacts**
Displays all stored contacts in a tabular format, showing:
- Full name
- Address
- Contact number

### 5. **Search for a Contact**
Users can search for contacts either by:
- Full Name
- Contact Number

### 6. **Exit the Program**
Users can exit the program gracefully at any time.

## How to Use
1. Download or clone the repository.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script:
   ```bash
   python AddressBook.py
