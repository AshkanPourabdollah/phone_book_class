import os

NUMBER_OF_CHARACTERS = 25


################################################## Functions ##########################################################
# Checking file exists
def check_file_exists(file_path):
    if not os.path.exists(file_path):
        file = open(file_path, 'x')
        file.close()


def table_character_space_creator(entry):
    return (NUMBER_OF_CHARACTERS - len(entry)) * " "


def table_creator(user_list):
    print(
        f'# \t| ' +
        f'Name{table_character_space_creator("Name")}| ' +
        f'Last Name{table_character_space_creator("last name")}|\t ' +
        f'Phone Number')
    print("======================================================================================")

    counter = 1
    for user in user_list:
        # Getting seperator form main part
        user = user[:-1]
        info = user.split(separator)
        name = info[0] + table_character_space_creator(info[0])
        last_name = info[1] + table_character_space_creator(info[1])
        phone = info[2] + table_character_space_creator(info[2])
        print(f'{counter} \t| {name}| {last_name}|\t {phone}')
        counter += 1


def search(file_path, entry):
    data = reading_file(file_path)

    # Returned list
    returned_list = []

    # Searching
    for line in data:
        if entry in line:
            returned_list.append(line)

    return returned_list


def title(title_text):
    print("=" * ((NUMBER_OF_CHARACTERS * 2) + len(title_text) + 2))
    print(table_character_space_creator('') + f'🔸{title_text}🔸')
    print("=" * ((NUMBER_OF_CHARACTERS * 2) + len(title_text) + 2))
    print()


def reading_file(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()


def append_to_file(file_path, line):
    with open(file_path, 'a') as f:
        f.write(line)


def validation_name_and_last_name(content):
    if content.isnumeric():
        print("🚫 Entry shouldn't have number !")
        return False
    elif not bool(content):
        print("🚫 Entry shouldn't be empty")
        return False
    elif "#" in content or "@" in content:
        print("🚫 Entry shouldn't contain # or @ !")
        return False
    elif len(content) > NUMBER_OF_CHARACTERS:
        print(f"🚫 Entry shouldn't be longer than {NUMBER_OF_CHARACTERS} characters")
        return False
    else:
        return True


def validation_phone(phone):
    if phone.isalpha():
        print("🚫 Phone shouldn't have character !")
        return False
    elif not bool(phone):
        print("🚫 Phone shouldn't be empty")
        return False
    elif "#" in phone or "@" in phone:
        print("🚫 Phone shouldn't contain # or @ !")
        return False
    elif len(phone) != 11:
        print(f"🚫 Phone should be 11 number")
        return False
    else:
        return True


def show_contacts_main_function(file_path):
    title('Show Contacts')
    data = reading_file(file_path)
    table_creator(data)


def add_contacts_main_function(file_path):
    title("Adding Contact")
    # Getting Name
    name = input("👤 Name >>> ").title().strip()
    # Validation Name
    if not validation_name_and_last_name(name):
        return False

    # Getting Last Name
    last_name = input("👤 Last Name >>> ").title().strip()
    # Validation Last Name
    if not validation_name_and_last_name(last_name):
        return False

    # Getting Phone
    phone = input("📞 Phone >>> ").strip()
    # Validation Phone
    if not validation_phone(phone):
        return False

    # adding to database
    content = f'{name}{separator}{last_name}{separator}{phone}\n'
    append_to_file(file_path, content)

    # showing suitable message
    print("✅ Your contact has been added successfully.")


def search_contacts_main_function(file_path):
    title('Searching Contacts')

    print("With which parameter do you want to search?")
    print('1️⃣ Name')
    print('2️⃣ Phone')
    search_choice = input("😃 Enter your choice >>> ")

    # Checking validation by entry
    if search_choice == "1":
        entry = input("👤 Name >>> ").title().strip()
        if not validation_name_and_last_name(entry):
            return False
    elif search_choice == "2":
        entry = input("📞 Phone >>> ").strip()
        if not validation_phone(entry):
            return False
    else:
        print("😐 Invalid choice")
        return False

    # searching and creating table form data
    data = search(file_path, entry)
    if len(data) == 0:
        print("🚫 There is no contact!")
    else:
        print("✅ Founded Contacts\n")
        table_creator(data)


################################################## Main part ##########################################################
file_name = 'database.txt'
separator = '###'
check_file_exists(file_name)

# Starting phone book
print('Hello and welcome to Computech phone book 📞')

# Menu
menu = '''
What do you want to do?
1️⃣ Show Contacts
2️⃣ Add Contact
3️⃣ Update Contact
4️⃣ Delete Contact
5️⃣ Search Contacts
6️⃣ Exit
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
        print("Thank you for using Computech phone book ! 😊")
        print("Programmed by : Ashkan Pourabdollah 😎")
        print('Have a nice time ! 👋')
        break
    else:
        print('😐 Invalid choice')
