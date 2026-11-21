# Here the mini (weekend) project, show the understanding of basics of python using cli based personal expense tracker

print(30*'=')
print(4*' ' + "MINI EXPENSE TRACKER" + 4*" ")
print(30*'=')

print("Welcome to your expense manager!" + "\n" + "Application started successfully.\n")
print(
    "1. Add Expense \n"+ 
    "2. View Expenses \n" + 
    "3. Total Spending \n" +
    "4. Spending By Category \n" +
    "5. Exit \n")

Expenses = []

while True:
  option = int(input("Choose an option:- "))
  
  if(option > 5 or option < 1):
    print("Invalid option! Please choose between 1 and 5.")
    pass
  
  else:
      if(option == 1):
        print('\n')
        print(10*"-" + " ADD EXPENSE " + 10*"-")
        Item_name = str(input("Enter the expense name: "))
        Item_cost = float(input("Enter amount:$ "))
        Item_category = str(input("Enter Category: ")).capitalize()
        
        expense_item = {
        "name": Item_name,
        "amount": Item_cost,
        "category": Item_category
        }

        Expenses.append(expense_item)
        print("Expense added successfully! \n")

      elif (option == 2):
        print(10*"=" + " YOUR EXPENSES "+ 10*"=")

        if not Expenses:
          print("No expenses recorded yet.")
        else:
          for expense in Expenses:
            print(f"Expense: {expense['name']}, Amount: ${expense['amount']}, Category: {expense['category']}")
        print("\n")
        print(21*"=")


      elif(option == 3):
        total = 0
        for expense in Expenses:
          total += expense['amount']
        print("Total expenses:$ ", total)


      elif(option == 4):
        print(10*"=" + " CATEGORY SUMMARY " + 10*"=")

        if not Expenses:
            print("No expenses to summarize.")
        else:
            category_totals = {}
            for expense in Expenses:
                cat = expense["category"]
                amt = expense["amount"]
                
                category_totals[cat] = category_totals.get(cat, 0) + amt

            for cat, total_amt in category_totals.items():
                print(f"{cat}: ${total_amt:.2f}")


        print(21*"=")


      else:
        print("Thank you for using Expense Tracker!")
        break