from expense import Expense

def main():
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = 'expenses.csv'
    while True:
        # Get user input for expense.
        expense = get_user_expense()
        # Write their expense to a file.
        save_expense_to_file(expense, expense_file_path)
        # Ask if the user wants to add another expense.
        another = input("Do you want to add another expense? (yes/no): ").strip().lower()
        if another != "yes":
            break
    # Read file and summarize expenses.
    summarize_expenses(expense_file_path)

def get_user_expense():
    print(f"\n🎯 Getting user expenses")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
    ]

    while True:
        print("Select a category:")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if 0 <= selected_index < len(expense_categories):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print(f"Invalid selection. Please enter a number {value_range}.")

def save_expense_to_file(expense: Expense, expense_file_path: str):
    print(f"\n🎯 Saving user expense {expense.name} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

def summarize_expenses(expense_file_path: str):
    print(f"\n🎯 Summarizing user expenses")
    try:
        with open(expense_file_path, "r") as f:
            lines = f.readlines()
            total_amount = 0.0
            category_totals = {}
            for line in lines:
                try:
                    name, category, amount = line.strip().split(',')
                    amount = float(amount)
                    total_amount += amount
                    if category in category_totals:
                        category_totals[category] += amount
                    else:
                        category_totals[category] = amount
                except ValueError as e:
                    print(f"Skipping line due to formatting error: {line}")
                    continue

            print(f"\nTotal Expenses: ${total_amount:.2f}")
            for category, total in category_totals.items():
                print(f"{category}: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses found.")

if __name__ == "__main__":
    main()
