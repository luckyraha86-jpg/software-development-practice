from tracker import add_expense, get_all_expenses, get_expenses_by_category, delete_expense


def main():
  while True:
    print("\n=================================")
    print("========= EXPENSE TRACKER =======")
    print("=================================")
    print("Choose the options you want to do:")
    print("1. Add expenses")
    print("2. View all expenses & Total")
    print("3. View expenses by category")
    print("4. Delete expense")
    print("5. Exit")

    try:
      choice = int(input("Choose (1-5): "))
    except ValueError:
      print("❌ Invalid input! Please enter a valid number (1-4).")
      continue

    if choice == 1:
      try:
        amount = float(input("Enter the amount: "))
      except ValueError:
        print("❌ Only numbers allowed for amount!")
        continue

      category = input("Enter category (e.g., Food, Travel): ")
      description = input("Description: ")

      add_expense(amount, category, description)

    elif choice == 2:
      expenses = get_all_expenses()

      if not expenses:
        print("\n📂 Khali dabba! Abhi तक koi expense add nahi kiya hai.")
      else:
        print("\n---------------------------------")
        print("📜 YOUR EXPENSE HISTORY:")
        print("---------------------------------")
        total_spent = 0
        for index, exp in enumerate(expenses, start=1):
          print(
              f"{index}. ₹{exp['amount']} | [{exp['category']}]"
              f" - {exp['description']}"
          )
          total_spent += exp["amount"]

        print("---------------------------------")
        print(f"💰 Total Spent: ₹{total_spent}")
        print("---------------------------------")

    elif choice == 3:
      target_category = input("Enter category to filter (e.g., Food): ")
      filtered_expenses, cat_total = get_expenses_by_category(target_category)

      if not filtered_expenses:
        print(f"\n❌ Is '{target_category}' category mein koi expense nahi mila.")
      else:
        print("\n---------------------------------")
        print(f"🎯 EXPENSES FOR CATEGORY: {target_category.upper()}")
        print("---------------------------------")
        for index, exp in enumerate(filtered_expenses, start=1):
          print(f"{index}. ₹{exp['amount']} - {exp['description']}")

        print("---------------------------------")
        print(f"💰 Total in '{target_category}': ₹{cat_total}")
        print("---------------------------------")
    elif choice == 4:
      all_expense = get_all_expenses()
      print("\n---------------------------------")
      print(f"🎯 EXPENSES")
      print("---------------------------------")
      for index, exp in enumerate(all_expense, start=1):
        print(f"{index}. ₹{exp['amount']} - {exp['description']}")

      target = int(input("Choose the category you want to delete: "))
      delete_expense(target)
      
    elif choice == 5:
      print("\n👋 System shutdown. Bye bye, take care!")
      break

    else:
      print("❌ Invalid choice! Please select between 1 and 5.")


if __name__ == "__main__":
  main()