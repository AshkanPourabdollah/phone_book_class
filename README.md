# 📞 Computech Phone Book

A simple **Command-Line Phone Book Application** written in **Python** that allows users to **store, view, search, update, and delete** contacts locally.  
This project is perfect for beginners who want to learn about **file handling**, **input validation**, and **basic CLI UI design** in Python.

---

## 🚀 Features

✅ Add new contacts (Name, Last Name, and Phone Number)  
✅ Show all saved contacts in a clean, formatted table  
✅ Search contacts by name or phone number  
✅ Update existing contacts  
✅ Delete contacts  
✅ Auto-create database file if it doesn’t exist  
✅ Input validation for both names and phone numbers  
✅ Simple and user-friendly command-line interface  

---

## 🧠 Concepts Used

This project demonstrates:
- **File Handling** (`open`, `readlines`, `write`, `append`)
- **String Manipulation**
- **Functions & Modular Programming**
- **Input Validation**
- **Formatted Table Output**
- **Loops and Conditional Statements**
- **Basic Error Handling**

---

## 🗂️ Project Structure

```
📁 ComputechPhoneBook
│
├── database.txt         # Stores all contacts
├── main.py              # Main Python script (contains all functionalities)
└── README.md            # Project documentation
```

---

## ⚙️ How It Works

1. When the program starts, it checks if `database.txt` exists — if not, it creates one automatically.  
2. You’ll see a menu like this:

```
Hello and welcome to Computech phone book 📞

What do you want to do?
1️⃣ Show Contacts
2️⃣ Add Contact
3️⃣ Update Contact
4️⃣ Delete Contact
5️⃣ Search Contacts
6️⃣ Exit
>>> 
```

3. Choose an option by typing the corresponding number.

---

## 🧩 Example Usage

### ➕ Adding a Contact
```
👤 Name >>> John
👤 Last Name >>> Doe
📞 Phone >>> 09121234567
✅ Your contact has been added successfully.
```

### 📋 Showing Contacts
```
#  | Name                     | Last Name                |   Phone Number
======================================================================================
1  | John                     | Doe                      |   09121234567
```

### 🔍 Searching
```
With which parameter do you want to search?
1️⃣ Name
2️⃣ Phone
😃 Enter your choice >>> 1
👤 Name >>> John

✅ Founded Contacts

#  | Name                     | Last Name                |   Phone Number
======================================================================================
1  | John                     | Doe                      |   09121234567
```

---

## 🧰 Requirements

You only need **Python 3.8+** installed on your system.

Check your version:
```bash
python --version
```

Run the script:
```bash
python main.py
```

---

## 🧼 Input Validation Rules

| Field | Validation |
|-------|-------------|
| **Name / Last Name** | Cannot contain numbers, `#`, or `@`, and must not be empty or longer than 25 characters. |
| **Phone Number** | Must be 11 digits, cannot contain letters or symbols, and cannot be empty. |

---

## 🗑️ Update & Delete

- **Update Contact**: Allows you to select a specific contact and modify its name, last name, or phone number.  
- **Delete Contact**: Lets you remove a contact by its number from the contact list.

---

## 🧑‍💻 Author

**👨‍💻 Ashkan Pourabdollah**  
Android & Backend Developer  
📚 University of Shahrekord Graduate  
💡 Passionate about Python and clean software design.

---

## 💬 Future Improvements

- Add export/import to CSV or JSON format  
- Add sorting and filtering  
- Create GUI version using Tkinter or PyQt  
- Add password-protection for data  

---

## 🪪 License

This project is open-source and available under the **MIT License**.  
Feel free to use, modify, and distribute it.

---

⭐ **If you like this project, don’t forget to give it a star on GitHub!**
