def menu():
    print("**** Calculator ****")
    print("1. Sum")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Clear ")
    print("6. Exit")


def operation(option, current_number):
    try:
        number = float(input("Enter the number for the operation: "))
    except ValueError as error:
        print(f"Error! You must enter a valid number: {error}")
        return current_number

    if option == 1:
        current_number = current_number + number  
        print(f"Updated result: {current_number}")
    elif option == 2:
        current_number = current_number - number 
        print(f"Updated result: {current_number}")
    elif option == 3:
        current_number = current_number * number
        print(f"Updated result: {current_number}")
    elif option == 4:
        if number == 0:
            print("Error! Division by zero is not allowed")
        else:
            current_number =  current_number / number
            print(f"Updated result: {current_number}")
    
    return current_number


def calculator():
    try:
        current_number = float(input("Enter the number for starting the operation: "))
    except ValueError as error:
        print(f"Error! You must enter a valid number: {error}")
        return current_number
    
    while True:
        menu()
        try:
            option = int(input("Select an option: "))
        except ValueError as ex:
            print(f"Error! Invalid option {ex}")
            continue
            
        if option == 5:
            current_number = 0
            print("Cleared")
            try:
                current_number = float(input("Enter the number for starting the operation: "))
            except ValueError as error:
                print(f"Error! You must enter a valid number: {error}")
                return current_number
        elif option == 6:
            print("Exiting")
            break
        elif option < 1 or option > 6:
            print("Error! Invalid option")
        else:
            current_number = operation(option, current_number)


if __name__ == "__main__":
    calculator()