"""
Phone Book Application
Developed by Ashkan Pourabdollah

A command-line phone book application that allows users to:
- Store and manage contacts (name, last name, phone number)
- View contacts in a formatted table
- Search, update, delete, and sort contacts
- Validate user input data

Features:
- File-based storage using 'database.txt'
- Input validation for names and phone numbers
- Table formatting for better readability
- Case-insensitive search functionality
- Sorting by name, last name, or phone number
"""

import os

# Constants for configuration
NUMBER_OF_CHARACTERS = 25  # Maximum characters for table formatting
NAME = 'name'  # Constant for name field
LAST_NAME = 'last_name'  # Constant for last name field
PHONE = 'phone'  # Constant for phone field


################################################## Functions ##########################################################

def check_file_exists(file_path):
    """Check if file exists, create empty file if it doesn't"""
    if not os.path.exists(file_path):
        with open(file_path, 'x'):
            pass  # Create empty file


def table_character_space_creator(entry):
    """Create spacing for table formatting based on entry length"""
    return (NUMBER_OF_CHARACTERS - len(entry)) * " "


def table_creator(user_list):
    """Display contacts in a formatted table"""
    # Print table header
    print(
        f'# \t| ' +
        f'Name{table_character_space_creator("Name")}| ' +
        f'Last Name{table_character_space_creator("last name")}|\t ' +
        f'Phone Number')
    print("======================================================================================")

    # Print each contact in table format
    counter = 1
    for user in user_list:
        user = user[:-1]  # Remove newline character
        info = user.split(separator)  # Split contact data
        name = info[0] + table_character_space_creator(info[0])  # Format name with spacing
        last_name = info[1] + table_character_space_creator(info[1])  # Format last name with spacing
        phone = info[2] + table_character_space_creator(info[2])  # Format phone with spacing
        print(f'{counter} \t| {name}| {last_name}|\t {phone}')  # Print formatted contact
        counter += 1


def search(file_path, entry):
    """Search for contacts containing the specified entry"""
    data = reading_file(file_path)  # Read all contacts
    returned_list = []  # Initialize results list

    # Search through each contact
    for line in data:
        if entry in line:  # Check if entry exists in contact
            returned_list.append(line)  # Add matching contact to results

    return returned_list


def title(title_text):
    """Display formatted title with decorative elements"""
    print("=" * ((NUMBER_OF_CHARACTERS * 2) + len(title_text) + 2))  # Print top border
    print(table_character_space_creator('') + f'🔸{title_text}🔸')  # Print centered title with icons
    print("=" * ((NUMBER_OF_CHARACTERS * 2) + len(title_text) + 2))  # Print bottom border
    print()


def clean_screen():
    """Clear the terminal screen based on operating system"""
    os.system('cls' if os.name == 'nt' else 'clear')  # Windows vs Unix/Linux/Mac


def waiting_for_enter():
    """Wait for user to press enter to continue"""
    print(NUMBER_OF_CHARACTERS * 3 * "=")  # Print separator
    input("\n⏭️ Please enter 'enter' key to continue...")  # Prompt user


def reading_file(file_path):
    """Read all lines from file and return as list"""
    with open(file_path, 'r') as f:
        return f.readlines()  # Return list of lines


def check_unique_phone_number(file_path, phone):
    """Check if phone number already exists in database"""
    data = reading_file(file_path)  # Read all contacts

    # Check each contact for duplicate phone
    for i in data:
        if phone in i:  # Phone number found
            return True

    return False  # Phone number is unique


def append_to_file(file_path, line):
    """Append a line to the file"""
    with open(file_path, 'a') as f:
        f.write(line)  # Write line to end of file


def change_order(user_list, order_by):
    """Reorder contacts based on specified field (name, last_name, phone)"""
    new_list = []  # Initialize reordered list

    # Reformat contacts based on ordering field
    for user in user_list:
        user = user[:-1]  # Remove newline
        name = user.split(separator)[0]  # Extract name
        last_name = user.split(separator)[1]  # Extract last name
        phone = user.split(separator)[2]  # Extract phone

        # Reorder fields based on sorting preference
        if order_by == NAME:
            new_list.append(f'{name}{separator}{last_name}{separator}{phone}')
        elif order_by == LAST_NAME:
            new_list.append(f'{last_name}{separator}{name}{separator}{phone}')
        else:
            new_list.append(f'{phone}{separator}{name}{separator}{last_name}')

    # Clear original list and sort new list
    user_list.clear()
    new_list.sort()  # Sort alphabetically/numerically

    # Restore original field order after sorting
    for new_user in new_list:
        if order_by == NAME:
            name, last_name, phone = new_user.split(separator)
        elif order_by == LAST_NAME:
            last_name, name, phone = new_user.split(separator)
        else:
            phone, name, last_name = new_user.split(separator)

        user_list.append(f'{name}{separator}{last_name}{separator}{phone}\n')  # Add formatted contact

    print(f"✅ Order changed based on << {order_by.title()} >>")
    return user_list


def override_file(file_path, user_list):
    """Overwrite file with new contact list"""
    with open(file_path, 'w') as f:
        for i in user_list:
            f.write(i)  # Write each contact to file


def validation_name_and_last_name(content):
    """Validate name and last name fields"""
    if content.isnumeric():  # Check if contains only numbers
        print("🚫 Entry shouldn't have number !")
        return False
    elif not bool(content):  # Check if empty
        print("🚫 Entry shouldn't be empty")
        return False
    elif "#" in content or "@" in content:  # Check for special characters
        print("🚫 Entry shouldn't contain # or @ !")
        return False
    elif len(content) > NUMBER_OF_CHARACTERS:  # Check length limit
        print(f"🚫 Entry shouldn't be longer than {NUMBER_OF_CHARACTERS} characters")
        return False
    else:
        return True  # Validation passed


def validation_phone(phone):
    """Validate phone number field"""
    if phone.isalpha():  # Check if contains letters
        print("🚫 Phone shouldn't have character !")
        return False
    elif not bool(phone):  # Check if empty
        print("🚫 Phone shouldn't be empty")
        return False
    elif "#" in phone or "@" in phone:  # Check for special characters
        print("🚫 Phone shouldn't contain # or @ !")
        return False
    elif len(phone) != 11:  # Check exact length requirement
        print(f"🚫 Phone should be 11 number")
        return False
    else:
        return True  # Validation passed


def show_contacts_main_function(file_path):
    """Main function to display all contacts"""
    title('Show Contacts')  # Display title
    data = reading_file(file_path)  # Read contacts

    # Check if database is empty
    if len(data) == 0:
        print("❌ There is no user in the database!")
        print("⚠️ Select second part to add new one!")
        print()
        return False

    table_creator(data)  # Display contacts in table


def add_contacts_main_function(file_path):
    """Main function to add new contact"""
    title("Adding Contact")

    # Get and validate name
    name = input("👤 Name >>> ").title().strip()
    if not validation_name_and_last_name(name):
        return False  # Validation failed

    # Get and validate last name
    last_name = input("👤 Last Name >>> ").title().strip()
    if not validation_name_and_last_name(last_name):
        return False  # Validation failed

    # Get and validate phone
    phone = input("📞 Phone >>> ").strip()
    if not validation_phone(phone):
        return False  # Validation failed

    # Check for duplicate phone number
    if check_unique_phone_number(file_path, phone):
        print("❌ There is already a contact with that phone number!")
        print("⚠️ Please try a new phone number!")
        return False

    # Add contact to database
    content = f'{name}{separator}{last_name}{separator}{phone}\n'
    append_to_file(file_path, content)

    # Confirm success
    clean_screen()
    print("✅ Your contact has been added successfully.")


def update_contact_main_function(file_path):
    """Main function to update existing contact"""
    title("Update Contact")

    # Get and validate phone number to update
    user_phone = input("Enter user phone >>> ").strip()
    if not validation_phone(user_phone):
        return False  # Validation failed

    data = reading_file(file_path)  # Read all contacts
    search_results = search(file_path, user_phone)  # Search for contact

    # Check if contact exists
    if len(search_results) == 0:
        print(f"❌ User not found with phone {user_phone}!")
        return False

    user = search_results[0]  # Get first matching contact

    # Display update options
    print("Which parameter do you want to update?")
    print("1️⃣ Name")
    print("2️⃣ Last Name")
    print("3️⃣ Name & Last Name")

    update_choice = input(">>> ").strip()

    # Extract current contact information
    name, last_name, phone = user[:-1].split(separator)

    # Update based on user choice
    if update_choice == '1':
        # Update name only
        name = input("New Name >>> ").title().strip()
        if not validation_name_and_last_name(name):
            return False  # Validation failed
    elif update_choice == '2':
        # Update last name only
        last_name = input("New Last Name >>> ").title().strip()
        if not validation_name_and_last_name(last_name):
            return False  # Validation failed
    elif update_choice == '3':
        # Update both name and last name
        name = input("New Name >>> ").title().strip()
        if not validation_name_and_last_name(name):
            return False  # Validation failed

        last_name = input("New Last Name >>> ").title().strip()
        if not validation_name_and_last_name(last_name):
            return False  # Validation failed
    else:
        print("😐 Invalid choice")
        return False

    # Remove old contact and add updated version
    data.remove(user)  # Remove old contact
    data.append(f'{name}{separator}{last_name}{separator}{phone}\n')  # Add updated contact

    # Save changes and reorder
    override_file(file_path, change_order(data, NAME))  # Save and sort by name

    print("✅ Your contact has been updated successfully.")


def delete_contact_main_function(file_path):
    """Main function to delete contact(s)"""
    title("Delete Contact")

    # Read contacts and check if database is empty
    data = reading_file(file_path)
    if len(data) == 0:
        print("❌ There is no user in the database!")
        print("⚠️ You should have contact to delete it")
        print("Am i right?! 😉")
        print()
        return False

    # Get search term for deletion
    deleting_entry = input("🔤 Please enter phone or a name you want to delete >>> ").title().strip()

    new_data = []  # Initialize list for contacts to keep
    user_counter = 0  # Counter for deleted contacts

    # Process deletion based on input type (phone or name)
    if deleting_entry.isnumeric():  # Input is phone number
        if not validation_phone(deleting_entry):
            print("⚠️ What you entered is not valid, please try again.")
            return False  # Validation failed

        # Filter contacts, keeping those that don't match
        for user in data:
            if not deleting_entry in user:  # Keep non-matching contacts
                new_data.append(user)
            else:  # Count matching contacts for deletion
                user_counter += 1
    else:  # Input is name
        if not validation_name_and_last_name(deleting_entry):
            print("⚠️ What you entered is not valid, please try again.")
            return False  # Validation failed

        # Filter contacts by name
        for user in data:
            if deleting_entry != user.split(separator)[0]:  # Keep non-matching names
                new_data.append(user)
            else:  # Count matching names for deletion
                user_counter += 1

    # Save updated contact list
    override_file(file_path, new_data)

    # Display deletion results
    if user_counter == 0:
        print('⚠️ There is no contact with this info exists!')
    else:
        print(f'✅ {user_counter} contact with this info deleted successfully!!')


def search_contacts_main_function(file_path):
    """Main function to search for contacts"""
    title('Searching Contacts')

    # Choose search criteria
    print("❓ With which parameter do you want to search?")
    print('1️⃣ Name')
    print('2️⃣ Phone')
    search_choice = input("😃 Enter your choice >>> ")

    clean_screen()
    # Get search term based on choice
    if search_choice == "1":  # Search by name
        entry = input("👤 Name >>> ").title().strip()
        if not validation_name_and_last_name(entry):
            return False  # Validation failed
    elif search_choice == "2":  # Search by phone
        entry = input("📞 Phone >>> ").strip()
        if not validation_phone(entry):
            return False  # Validation failed
    else:
        print("😐 Invalid choice")
        return False

    # Perform search and display results
    data = search(file_path, entry)
    if len(data) == 0:
        print("🚫 There is no contact!")
    else:
        print("✅ Founded Contacts :\n")
        table_creator(data)  # Display results in table


def order_contacts_list_main_function(file_path):
    """Main function to sort contacts"""
    title("Ordering Contacts")

    # Choose sorting criteria
    print("❓ With which parameter do you want to order?")
    print("1️⃣ Name")
    print("2️⃣ Last Name")
    print("3️⃣ Phone")
    order_choice = input('>>> ')

    data = reading_file(file_path)  # Read all contacts

    # Sort based on user choice
    if order_choice == "1":  # Sort by name
        override_file(file_path, change_order(data, NAME))
    elif order_choice == "2":  # Sort by last name
        override_file(file_path, change_order(data, LAST_NAME))
    elif order_choice == "3":  # Sort by phone
        override_file(file_path, change_order(data, PHONE))
    else:
        print("😐 Invalid choice")  # Invalid input


################################################## Main part ##########################################################

# Configuration
file_name = 'database.txt'  # Database file name
separator = '###'  # Field separator in database

# Initialize database file
check_file_exists(file_name)

# Welcome message
print('Hello and welcome to Computech phone book 📞')

# Main menu
menu = '''
❓ What do you want to do?
1️⃣ Show Contacts
2️⃣ Add Contact
3️⃣ Update Contact
4️⃣ Delete Contact
5️⃣ Search Contacts
6️⃣ Order Contacts List
7️⃣ Exit
>>> '''

# Main application loop
while True:
    clean_screen()  # Clear screen
    choice = input(menu)  # Get user choice
    clean_screen()  # Clear screen again

    # Execute function based on user choice
    if choice == '1':
        show_contacts_main_function(file_name)  # Show all contacts
    elif choice == '2':
        add_contacts_main_function(file_name)  # Add new contact
    elif choice == '3':
        update_contact_main_function(file_name)  # Update existing contact
    elif choice == '4':
        delete_contact_main_function(file_name)  # Delete contact
    elif choice == '5':
        search_contacts_main_function(file_name)  # Search contacts
    elif choice == '6':
        order_contacts_list_main_function(file_name)  # Sort contacts
    elif choice == '7':
        # Exit application
        print("Thank you for using Computech phone book ! 😊")
        print("Programmed by : Ashkan Pourabdollah 😎")
        print('Have a nice time ! 👋')
        break  # Exit loop
    else:
        print('😐 Invalid choice')  # Handle invalid input

    # Pause before returning to menu
    waiting_for_enter()
