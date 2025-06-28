import json

def save_data(manager, file="data.json"):
    list_of_categories = []
    for category_object in manager.categories:
        list_of_categories.append(category_object.name)


    list_of_movements = []
    for movement_object in manager.movements:
        movement_data = {
            "type": movement_object.type,
            "title": movement_object.title,
            "amount": movement_object.amount,
            "category": movement_object.category,
            "date": movement_object.date
        }
        list_of_movements.append(movement_data)


    data_dict = {
        "categories": list_of_categories,
        "movements": list_of_movements
    }


    with open(file, "w", encoding="utf-8") as json_file:
        json.dump(data_dict, json_file, indent=4)
    print("Data was saved successfully.")


def load_data(manager, file="data.json"):
    try:                                             
        with open(file, "r", encoding="utf-8") as json_file:
            data_json = json.load(json_file)


        manager.categories.clear()
        for name in data_json.get("categories", []):
            manager.add_category(name)         


        manager.movements.clear()
        for item in data_json.get("movements", []):
            manager.add_movement(
                item["type"],
                item["title"],
                item["amount"],
                item["category"]
            )
            manager.movements[-1].date = item["date"]   
        print("Data was loaded successfully.")          
    except FileNotFoundError:
        print("No existing data file found.")


