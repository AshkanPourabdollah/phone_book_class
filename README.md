# 📞 Computech Phone Book

A simple and efficient **Command-Line Phone Book Application** written
in **Python**, allowing users to easily **add, display, search, update,
delete, and sort** contacts stored locally in a text file.

This project is great for learning **file handling**, **input
validation**, **modular programming**, and building a clean **CLI-based
user interface**.

------------------------------------------------------------------------

## 🚀 Features

### 📋 Contact Management

-   ➕ **Add new contacts** (Name, Last Name, Phone Number)
-   📄 **Show all contacts** in a clean, formatted table
-   🔍 **Search contacts** by name or phone number
-   ✏️ **Update existing contacts**
-   🗑️ **Delete contacts** by name or phone
-   🔃 **Sort contacts** by:
    -   Name
    -   Last Name
    -   Phone Number

### 💡 Additional Functionalities

-   📁 Automatically creates `database.txt` if not found\
-   🔒 Strong input validation\
-   🔠 Case-insensitive search\
-   🧹 Clean and user-friendly CLI interface

------------------------------------------------------------------------

## 🧠 Concepts Used

-   File Handling (`open`, `readlines`, `write`, `append`)
-   String Manipulation
-   Functions & Modular Programming
-   Input Validation
-   Formatted Table Output
-   Loops and Conditionals
-   Basic Error Handling

------------------------------------------------------------------------

## 🗂️ Project Structure

    📁 ComputechPhoneBook
    │
    ├── database.txt         # Stores all contacts
    ├── main.py              # Main Python script with all functionalities
    └── README.md            # Project documentation

------------------------------------------------------------------------

## ⚙️ How to Run

Make sure Python 3.8+ is installed.

Check Python version:

``` bash
python --version
```

Run the script:

``` bash
python main.py
```

------------------------------------------------------------------------

## 🧼 Input Validation Rules

  -----------------------------------------------------------------------
  Field                               Rules
  ----------------------------------- -----------------------------------
  **Name / Last Name**                No numbers, no `#`, `@`, not empty,
                                      max 25 characters

  **Phone Number**                    Must be exactly 11 digits, no
                                      letters, no symbols
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🧩 Example Usage

### ➕ Adding a Contact

    👤 Name >>> John
    👤 Last Name >>> Doe
    📞 Phone >>> 09121234567
    ✅ Your contact has been added successfully.

### 📋 Showing Contacts

    #  | Name                     | Last Name                |   Phone Number
    ======================================================================================
    1  | John                     | Doe                      |   09121234567

### 🔍 Searching

    With which parameter do you want to search?
    1️⃣ Name
    2️⃣ Phone
    😃 Your choice >>> 1
    👤 Name >>> John

------------------------------------------------------------------------

## 🧑‍💻 Author

**Ashkan Pourabdollah**\
Android & Backend Developer\
Passionate about Python and clean software design.
Owner of **Computech** company!
