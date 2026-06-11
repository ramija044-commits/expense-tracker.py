# Expense Tracker Program

print("===== EXPENSE TRACKER =====")

total_expense = 0

while True:
    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    try:
        amount = float(expense)
        total_expense += amount
        print(f"Added: ₹{amount:.2f}")
    except ValueError:
        print("Please enter a valid number!")

print("\n===== EXPENSE SUMMARY =====")
print(f"Total Spent: ₹{total_expense:.2f}")
print("Thank you for using Expense Tracker!")
