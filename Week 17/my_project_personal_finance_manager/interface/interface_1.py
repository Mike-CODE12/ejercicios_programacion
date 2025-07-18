import FreeSimpleGUI as sg
from models.models_1 import FinanceManager
from files.files_j import save_data, load_data
from logic.logic_1 import get_balance_summary

def create_main_window():
    layout = [
        [sg.Text("Personal Finance Manager", font=("Helvetica", 16), justification="center", expand_x=True)],
        [sg.Table(values=[],
                headings=["Type", "Title", "Amount", "Category", "Date"],
                key="TABLE_MOVEMENTS",
                auto_size_columns=False,
                justification="center",
                col_widths=[10, 20, 10, 15, 20],
                expand_x=True,
                expand_y=True,
                num_rows=10)],
        [sg.Button("Add Category"), sg.Button("Add Income"), sg.Button("Add Expense")],
        [sg.Text("Balance: "), sg.Text("0", key="TEXT_BALANCE", font=("Helvetica", 12))],
        [sg.Button("Exit")]
    ]
    return sg.Window("Finance Manager", layout, finalize=True, resizable=True)

def create_add_category_window():
    layout = [
        [sg.Text("Enter category name:")],
        [sg.Input(key="INPUT_CATEGORY_NAME")],
        [sg.Button("Add"), sg.Button("Cancel")]
    ]
    return sg.Window("Add Category", layout, modal=True, finalize=True)

def create_add_movement_window(movement_type, category_names):
    layout = [
        [sg.Text("Title:"), sg.Input(key="INPUT_TITLE")],
        [sg.Text("Amount:"), sg.Input(key="INPUT_AMOUNT")],
        [sg.Text("Category:"), sg.Combo(category_names, key="COMBO_CATEGORY")],
        [sg.Button("Add"), sg.Button("Cancel")]
    ]
    title = f"Add {movement_type}"
    return sg.Window(title, layout, modal=True, finalize=True)

def update_table_and_balance(window, manager):
    table_data = [[variable.type, variable.title, variable.amount, variable.category, variable.date] for variable in manager.movements]
    window["TABLE_MOVEMENTS"].update(values=table_data)

    balance_data = get_balance_summary(manager)
    balance_text = f"Income: {balance_data['total_income']} | Expense: {balance_data['total_expense']} | Final: {balance_data['final_balance']}"
    window["TEXT_BALANCE"].update(balance_text)

def run_interface():
    manager = FinanceManager()
    load_data(manager)

    main_window = create_main_window()
    update_table_and_balance(main_window, manager)

    category_window = None
    movement_window = None

    while True:
        try:
            window, event, values = sg.read_all_windows()


            if event == sg.WIN_CLOSED or event == "Exit":
                if window == main_window:
                    break
                else:
                    window.close()
                    if window == category_window:
                        category_window = None
                    if window == movement_window:
                        movement_window = None
                    continue

            if window == main_window:
                if event == "Add Category":
                    if category_window is None:
                        category_window = create_add_category_window()

                elif event == "Add Income" or event == "Add Expense":
                    if not manager.categories:
                        sg.popup_error("Please add at least one category first.")
                    else:
                        if movement_window is None:
                            movement_type = "Income" if event == "Add Income" else "Expense"
                            category_names = [category.name for category in manager.categories]
                            movement_window = create_add_movement_window(movement_type, category_names)

            elif window == category_window:
                if event == "Add":
                    category_name = values["INPUT_CATEGORY_NAME"].strip()
                    if not category_name:
                        sg.popup_error("Please enter a category name.")
                    else:
                        manager.add_category(category_name)
                        update_table_and_balance(main_window, manager)
                        save_data(manager)
                        category_window.close()
                        category_window = None
                elif event == "Cancel":
                    category_window.close()
                    category_window = None

            elif window == movement_window:
                if event == "Add":
                    title = values.get("INPUT_TITLE", "").strip()
                    amount_str = values.get("INPUT_AMOUNT", "").strip()
                    category = values.get("COMBO_CATEGORY", "")

                    if not title or not amount_str or not category:
                        sg.popup_error("Please fill in all fields.")
                    else:
                        try:
                            amount = float(amount_str)

                            if amount < 0:
                                sg.popup_error("Amount must be a positive number or zero number.")
                                continue

                            movement_type = movement_window.Title.split(" ")[1]  
                            manager.add_movement(movement_type, title, amount, category)
                            update_table_and_balance(main_window, manager)
                            save_data(manager)
                            movement_window.close()
                            movement_window = None
                        except ValueError:
                            sg.popup_error("Amount must be a number.")
                elif event == "Cancel":
                    movement_window.close()
                    movement_window = None

        except Exception as e:
            print(f"Exception caught in main loop: {e}")

    main_window.close()
    save_data(manager)
