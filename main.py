import os


NUMBER_OF_CHARACTERS = 25
NAME = 'name'
PHONE = 'phone'
################################################## Functions ##########################################################
# Checking file exists
def check_file_exists(file_path):
    if not os.path.exists(file_path):
        file = open(file_path, 'x')
        file.close()

def search(file_path, search_by, entry):
    data = reading_file(file_path)
    for line in data:
        if line.split(seperator)[0 if search_by == NAME else 2] == entry:
            return line

def reading_file(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()

def append_to_file(file_path, line):
    with open(file_path, 'a') as f:
        f.write(line)

def table_creator(entry):
    return (NUMBER_OF_CHARACTERS - len(entry)) * " "

def validation_name_and_last_name(content):
    if content.isnumeric():
        print("Entry shouldn't have number !")
        return False
    elif not bool(content):
        print("Entry shouldn't be empty")
        return False
    elif "#" in content or "@" in content:
        print("Entry shouldn't contain # or @ !")
        return False
    elif len(content) > NUMBER_OF_CHARACTERS:
        print(f"Entry shouldn't be longer than {NUMBER_OF_CHARACTERS} characters")
        return False
    else:
        return True

def validation_phone(phone):
    if phone.isalpha():
        print("Phone shouldn't have character !")
        return False
    elif not bool(phone):
        print("Phone shouldn't be empty")
        return False
    elif "#" in phone or "@" in phone:
        print("Phone shouldn't contain # or @ !")
        return False
    elif len(phone) != 11:
        print(f"Phone should be 11 number")
        return False
    else:
        return True

def show_contacts_main_function(file_path):
    data = reading_file(file_path)


    print(f'Name{table_creator("Name")}|\t Last name{table_creator("last name")}|\t  phone number')
    print("======================================================================================")
    for user in data:
        # Getting seperator form main part
        user = user[:-1]
        info = user.split(seperator)
        print(f'{info[0]}{table_creator(info[0])}|\t {info[1]}{table_creator(info[1])}|\t {info[2]}{table_creator(info[2])}')

def add_contacts_main_function(file_path):
    # Getting Name
    name = input("Name >>> ").title().strip()
    # Validation Name
    if not validation_name_and_last_name(name):
        return False

    # Getting Last Name
    last_name = input("Last Name >>> ").title().strip()
    # Validation Last Name
    if not validation_name_and_last_name(last_name):
        return False

    # Getting Phone
    phone = input("Phone >>> ").strip()
    # Validation Phone
    if not validation_phone(phone):
        return False

    # adding to database
    content = f'{name}{seperator}{last_name}{seperator}{phone}\n'
    append_to_file(file_path, content)

    # showing suitable message
    print("✅ Your contact has been added successfully.")

def search_contacts_main_function(file_path):
    print("With which parameter do you want to search?")
    print('1) Name')
    print('2) Phone')
    search_choice = input("Enter your choice: ")
    if search_choice == "1":
        name = input("Name >>> ").title().strip()
        if not validation_name_and_last_name(name):
            return False

        # searching
        print(search(file_path, NAME, name))

    elif search_choice == "2":
        phone = input("Phone >>> ").strip()
        if not validation_phone(phone):
            return False

        # searching
        print(search(file_path, PHONE, phone))

    else:
        print("Invalid choice")

################################################## Main part ##########################################################
file_name = 'database.txt'
seperator = '###'
check_file_exists(file_name)

# Menu
menu = '''
Hello and welcome to Computech phone book 📞

What do you want to do?
1) Show Contacts
2) Add Contact
3) Update Contact
4) Delete Contact
5) Search Contacts
6) Exit
>>> '''

while True:
    choice = input(menu)

    if choice == '1':
        show_contacts_main_function(file_name)
    elif choice == '2':
        add_contacts_main_function(file_name)
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        search_contacts_main_function(file_name)
    elif choice == '6':
        print("Thank you for using Computech phone book! 😊")
        break
    else:
        print('Invalid choice')
