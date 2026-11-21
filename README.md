Mini Expense Tracker

A simple command-line based personal expense tracker developed using Python. It allows users to add expenses, view recorded transactions, calculate total spending, and generate category-wise expense summaries.

Built as a beginner weekend project to practice Python fundamentals through hands-on implementation.

Features

- Add Expense: Enter an expense name, amount, and category.
- View Expenses: Display all recorded expenses.
- Total Spending: Calculate the sum of all recorded expenses.
- Category Summary: Group expenses by category and calculate their individual totals.
- Interactive Menu: Navigate between different operations using a command-line menu.


Concepts Practiced

- Variables and Data Types
- "input()" and "print()"
- Conditional Statements ("if-elif-else")
- "while" and "for" loops
- Lists and Dictionaries
- Type Conversion ("int()", "float()")
- Basic Arithmetic and Aggregation

---

Getting Started

Prerequisites

- Python 3 installed on your system.
- A terminal or command-line interface.

Run Locally

1. Clone the repository

git clone https://github.com/MOHDYASIR-315/mini-expense-tracker.git

2. Navigate to the project directory

cd mini-expense-tracker

3. Run the application

python main.py

---

Application Preview

1. Main Menu
==============================
     MINI EXPENSE TRACKER
==============================

Welcome to your expense manager!
Application started successfully.

1. Add Expense
2. View Expenses
3. Total Spending
4. Spending By Category
5. Exit

Choose an option:-

2. Add Expense

Enter the expense details when prompted.

Example Input:

Choose an option:- 1

---------- ADD EXPENSE ----------

Enter the expense name: Lunch
Enter amount:$ 120
Enter Category: Food

Expense added successfully!

3. View Expenses

Displays all expenses recorded during the current session.

Example Output:

========== YOUR EXPENSES ==========

Expense: Lunch, Amount: $120.0, Category: Food
Expense: Bus Ticket, Amount: $40.0, Category: Transport
Expense: Notebook, Amount: $80.0, Category: Education
Expense: Coffee, Amount: $60.0, Category: Food

=====================

4. Total Spending

Calculates the combined amount of all recorded expenses.

Example Output:

Total expenses:$ 300.0

5. Spending By Category

Calculates the total spending for each category.

Example Output:

========== CATEGORY SUMMARY ==========

Food: $180.00
Transport: $40.00
Education: $80.00

=====================

6. Exit

Closes the application.

Thank you for using Expense Tracker!

---

Project Structure

mini-expense-tracker/
│
├── main.py
└── README.md

Current Limitations

- Expenses are stored in a Python list of dictionaries.
- Data exists only while the application is running.
- Recorded expenses are not saved after exiting the application.
- Invalid non-numeric inputs may cause the program to terminate.
- Expense names, categories, and amounts have limited validation.

Future Improvements

- Implement functions for better code organization.
- Add input validation and exception handling.
- Introduce permanent data storage using JSON.
- Add transaction search and deletion.
- Explore data analysis and visualization.

---

Project Status

Version 1.0 — Initial Implementation

An independent beginner-level project focused on applying Python fundamentals to build a functional command-line application.