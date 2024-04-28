
class Expense:
    def __init__(self,date,description,amount):
        self.date = date
        self.description = description
        self.amount = amount
    

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self,expense):
        self.expenses.append(expense)
    
    def remove_expense(self,index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed successfully.")
        else:
            print("Invalid expense index.")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expense found.")
        else:
            print("Expense list:")
            for index, expense in enumerate(self.expenses):
                print(f"{index+1}. \tDate:{expense.date} \tDescription:{expense.description} \tAmount:{expense.amount}")
    
    def total_expense(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expense: {total:.2f}")


print("\n Expense Tracker Application")
tracker = ExpenseTracker()

while True:
    print("\n Expense Tracker Menu:")
    print("1. Add Expense")
    print("2. Remove Expense")
    print("3. View Expense")
    print("4. Total Expense")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        date = input("Enter the date (YYYY-MM-DD): ")
        description = input("Enter the description: ")
        amount = float(input("Enter the amount: "))
        expense = Expense(date,description,amount)
        tracker.add_expense(expense)
        print("Expense added successfully.")
    elif choice == '2':
        index = int(input("Enter index of expense:"))
        tracker.remove_expense(index-1)
    elif choice == '3':
        tracker.view_expenses()
    elif choice == '4':
        tracker.total_expense()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please choose right option.")