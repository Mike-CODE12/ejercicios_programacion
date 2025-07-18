from models.models_1 import FinanceManager

def test_add_category_result_adds_new_category():
    manager = FinanceManager()
    manager.add_category("Food")
    assert len(manager.categories) == 1
    assert manager.categories[0].name == "Food"

def test_add_category_result_does_not_add_duplicate():
    manager = FinanceManager()
    manager.add_category("Transport")
    manager.add_category("Transport")  
    assert len(manager.categories) == 1

def test_add_movement_result_adds_movement_if_category_exists():
    manager = FinanceManager()
    manager.add_category("Salary")
    manager.add_movement("Income", "June salary", 1500, "Salary")
    assert len(manager.movements) == 1
    movement = manager.movements[0]
    assert movement.type == "Income"
    assert movement.title == "June salary"
    assert movement.amount == 1500
    assert movement.category == "Salary"

def test_add_movement_result_does_not_add_if_category_missing():
    manager = FinanceManager()
    manager.add_category("Utilities")
    manager.add_movement("Expense", "Electric bill", 100, "Food")  
    assert len(manager.movements) == 0

def test_get_total_balance_result_correctly_calculates_balance():
    manager = FinanceManager()
    manager.add_category("Salary")
    manager.add_category("Groceries")
    manager.add_movement("Income", "Salary May", 2000, "Salary")
    manager.add_movement("Expense", "Supermarket", 200, "Groceries")
    manager.add_movement("Expense", "Market", 100, "Groceries")
    balance = manager.get_total_balance()
    assert balance == 1700 

def test_get_total_balance_returns_zero_when_no_movements():
    manager = FinanceManager()
    balance = manager.get_total_balance()
    assert balance == 0

def test_add_movement_result_adds_multiple_movements_of_a_same_category():
    manager = FinanceManager()
    manager.add_category("Entertainment")
    manager.add_movement("Expense", "Movie ticket", 15, "Entertainment")
    manager.add_movement("Expense", "Concert ticket", 45, "Entertainment")
    assert len(manager.movements) == 2

def test_add_category_in_a_sensitive_check_case():
    manager = FinanceManager()
    manager.add_category("Health")
    manager.add_category("health")  
    assert len(manager.categories) == 1
