# logic.py
def filter_movements_by_type(finance_manager, type_of_the_entered_movement):
    filtered_movements = []
    for movement in finance_manager.movements:
        if movement.type == type_of_the_entered_movement:
            filtered_movements.append(movement)
    return filtered_movements

def get_movements_by_category(finance_manager, category_name):
    filtered_movements = []
    for movement in finance_manager.movements:
        if movement.category == category_name:
            filtered_movements.append(movement)
    return filtered_movements

def get_total_amount_by_type(finance_manager, type_of_the_entered_movement):
    total_amount = 0
    for movement in finance_manager.movements:
        if movement.type == type_of_the_entered_movement:
            total_amount += movement.amount
    return total_amount

def get_balance_summary(finance_manager):
    total_income = get_total_amount_by_type(finance_manager, "Income")
    total_expense = get_total_amount_by_type(finance_manager, "Expense")
    final_balance = total_income - total_expense
    return {        
        "total_income": total_income,
        "total_expense": total_expense,
        "final_balance": final_balance}