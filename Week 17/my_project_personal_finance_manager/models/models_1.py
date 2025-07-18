from datetime import datetime  

class Category:
    def __init__(self, name):
        self.name = name

class Movement:
    def __init__(self, type_of_movement, title, amount, category, date=None):
        self.type = type_of_movement       
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M")

class FinanceManager:
    def __init__(self):
        self.categories = []
        self.movements = []

    def add_category(self, name):
        if not name or not name.strip():
            print("Category name cannot be empty.")
            return False
        normalized_name = name.strip().lower() 
        already_present = False
        for reviewer in self.categories:
            if reviewer.name.lower() == normalized_name:
                already_present = True
                print("That category is already present")
                break
        if not already_present:
            self.categories.append(Category(name.strip()))
            print("New category was added")


    def add_movement(self, type_of_movement, title, amount, category):
        already_present = False
        for reviewer in self.categories:
            if reviewer.name == category:
                already_present = True
                break
        if not already_present:
            print("The category of the movement does not exist")
            return
        self.movements.append(Movement(type_of_movement, title, amount, category, date=None))
        print("New movement was added")


    def get_total_balance(self):
        total_income = 0
        for income in self.movements:
            if income.type == "Income":
                total_income += income.amount
        total_expense = 0
        for expense in self.movements:
            if expense.type == "Expense":
                total_expense += expense.amount
        return total_income - total_expense
