print("Welcome to Expense Tracker.")
print("====Menu====")

print("1. Add Expense")
print("2. View Expenses")
print("3. Total Expenses")
print("4. Exit")
expenses = []
while True:

    choice = int(input("Please enter your choice: "))

    # Add Expenses
    
    if choice == 1:
        Date = (input("Enter the date of expenses: ")).strip()
        Category = input("Please enter the category of your expenses: ").strip()
        Description = input("Please enter the more detail of your expenses: ").strip()
        Amount = float(input("Please enter the amount: "))
        expense = {
        "Date" : Date,
        "Category" : Category,
        "Description" : Description,
        "Amount" : Amount
        }
        expenses.append(expense)
        print("\nExpenses are added successfully! ")

    # View Expenses

    elif(choice == 2) :
    
        if(len(expenses) == 0):
            print("No Expenses added. Please add some expenses. ")
        else:
            print("\nHere is your Expenses.")
            count = 1
            for item in expenses:
                print(f"expenses {count}, {item['Date']}, {item['Category']}, {item['Description']}, {item['Amount']}")
                count += 1

    # View Total Expense 

    elif choice == 3:
        Total = 0
        for item in expenses:
            Total += item["Amount"]
            print(f"Total Expense is: {Total}")

    # Exist 

    elif choice == 4:
        print("Thank you for using our app. ")
        break
    else:
        print("Invalid choice. Please Try Again!")
