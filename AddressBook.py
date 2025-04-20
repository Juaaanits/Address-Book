'''
Final Project: Address Book Management System
Course: Programming Logic and Design
Objective:
Create a console-based Address Book Management System that allows users to store, edit, delete, view, and search for contacts using Python.
'''
full_names = []
first_name_list = []
last_name_list = []
addresses = []
contact_numbers = []
answers = list(range(1, 100))
run = True

def print_intro():
    print("===============================================================Welcome to Address Book=====================================")
    print("What do you want to do? ")
    print("1. Add a contact. \n2. Edit a contact \n3. Delete a contact \n4. View all contacts \n5. Search for a contact \n6. Exit a program")

    choice = int(input("\nPick one that you want to do: "))
    return choice

def add_contact():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    address = input("Address: ")
    contact_num = input("Contact Number: ")
    while not contact_num.isdigit():
        contact_num = input("Enter a valid Contact Number (digits only): ")

    first_name_list.append(first_name)
    last_name_list.append(last_name)
    full_names.append(first_name + " " + last_name)
    addresses.append(address)
    contact_numbers.append(contact_num)
    print("Your inputs are successfully added. ")

def edit_contact():
    print('''
        1. Full Name
        2. Address
        3. Contact Number
    ''')
    while True:
        try:
            edit_choice = int(input("What do you want to edit? (1/2/3): "))
            if edit_choice in range(1, 4):
                break
            else:
                print("Please enter a valid choice (1/2/3).")   
        except ValueError:
            print("Invalid input! Please enter a number (1/2/3).")
        
        if edit_choice == 1:
            name_to_edit = input("Enter the full name you want to edit: ")
            if name_to_edit in full_names:
                new_name = input("Please enter your new name: ")
                index = full_names.index(name_to_edit)
                full_names[index] = new_name
                first, last = new_name.split(" ", 1)
                first_name_list[index] = first
                last_name_list[index] = last
                print("Contact selected updated!")
            else:
                print("Contact not found!")
                
        if edit_choice == 2:
            address_to_edit = input("Enter the address you want to edit: ")
            if address_to_edit in addresses:
                new_address = input("Please enter your new address: ")
                for i in range(len(addresses)):
                    if addresses[i] == address_to_edit:
                        addresses[i] = new_address
                        print("Contact selected updated!")
        
        if edit_choice == 3:
            contact_num_to_edit = input("Enter the contact number you want to edit: ")
            if contact_num_to_edit in contact_numbers:
                new_contact_num = input("Please enter your contact number ")
                for i in range(len(contact_numbers)):
                    if contact_numbers[i] == contact_num_to_edit:
                        contact_numbers[i] = new_contact_num
                        print("Contact selected updated!")
    
def delete_contact():
    name_to_delete = input("Enter the full name you want to delete: ")
    contact_num_to_delete = input("Enter the contact number you want to delete: ")
    if name_to_delete in full_names:
        index_name = full_names.index(name_to_delete)
        if contact_num_to_delete == contact_numbers[index_name]:
            full_names.pop(index_name)
            first_name_list.pop(index_name)
            last_name_list.pop(index_name)
            addresses.pop(index_name)
            contact_numbers.pop(index_name)
            print("Contact selected deleted!")
        else:
            print("Contact not found!")
            print("The contact number doesn't match the provided name!")
    else:
        print("Contact not found!")
        print("Please check the name and contact number you entered. ")

def view_contact():
    print("{:<20} {:<30} {:<15}".format("NAME", "ADDRESS", "PHONE NUMBER"))
    for i in range(len(full_names)):
        print("{:<20} {:<30} {:<15}".format(full_names[i], addresses[i], contact_numbers[i]))
        print("===============================================================")
    
def search_contact():
    print('''
Search by: 
    1. Full Name
    2. Contact Number
    ''')
    search_option = int(input("Choose an option (1/2): "))
    if search_option == 1:
        name_search = input("Enter Full Name: ").strip()
        if name_search in full_names:
            index = full_names.index(name_search)
            print("Contact found!")
            print("Name: ", full_names[index])
            print("Address: ", addresses[index])
            print("Contact Number: ", contact_numbers[index])
        else:
            print("Contact not found!")
    elif search_option == 2:
        contact_search = input("Enter Contact Number: ").strip()
        if contact_search in contact_numbers:
            index = contact_numbers.index(contact_search)
            print("Contact found!")
            print("Name: ", full_names[index])
            print("Address: ", addresses[index])
            print("Contact Number: ", contact_numbers[index])
        else:
            print("Contact not found!")
    else:
        print("Invalid option!")
    
def run_the_program():
    while True:
        option = print_intro()
        if option == 1:
            add_contact()
        elif option == 2:
            edit_contact()
        elif option == 3:
            delete_contact()
        elif option == 4:
            view_contact()
        elif option == 5:
            search_contact()
        elif option == 6:
            print("===============================================================")
            print("Thank you for using the Address Book Management System!")
            print("Exiting the program...")
            exit()
        else:
            print("Wrong input!")

if __name__ == "__main__":
    run_the_program()


