import json
import os

# JSON file ka naam jahan data save hoga
FILENAME = "expense_tracker/expenses.json"


def load_expenses():
  """JSON file se saare purane kharche load karne ke liye"""
  # Agar file hi nahi hai, toh empty list return kar do
  if not os.path.exists(FILENAME):
    return []

  try:
    with open(FILENAME, "r") as file:
      return json.load(file)
  except json.JSONDecodeError:
    # Agar file khali ya corrupt ho toh error na aaye, empty list mile
    return []


def save_expenses(expenses):
  """Saare kharcho ko wapas expenses.json file mein save karne ke liye"""
  with open(FILENAME, "w") as file:
    # indent=4 se JSON file saaf-suthri aur readable format mein save hoti hai
    json.dump(expenses, file, indent=4)


def add_expense(amount, category, description):
  """Naya expense list mein jod kar file mein save karega"""
  expenses = load_expenses()

  # Naye expense ka ek dictionary (object) banaya
  new_expense = {
      "amount": float(amount),
      "category": category,
      "description": description,
  }

  # List ke andar naya expense add kar diya
  expenses.append(new_expense)

  # Updated list ko wapas file mein save kar diya
  save_expenses(expenses)
  print(f"✅ Success: Expense of ₹{amount} added successfully!")

# def filtering(expenses):


def get_all_expenses():
  """Saare expenses ki list return karega"""
  return load_expenses()

def get_expenses_by_category(target_category):
  """Kisi specific category ke expenses aur uska total return karega"""
  expenses = load_expenses()

  # Case-insensitive match ke liye lower() use kar rahe hain (jaise "Food" aur "food" dono match ho jayein)
  filtered_expenses = [
      exp
      for exp in expenses
      if exp["category"].strip().lower() == target_category.strip().lower()
  ]

  total_amount = sum(exp["amount"] for exp in filtered_expenses)

  return filtered_expenses, total_amount

def delete_expense(target):
  exp = load_expenses()
  exp.remove(exp[target-1])
  save_expenses(exp)
  print(f"The expense: {target} successfully removed from the database")