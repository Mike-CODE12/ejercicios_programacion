#1Necesito mostrar un menú
#2Necesito ejecutar las tareas de cada una de las funciones y 4 de esas 6 funciones son matemáticas, por es lo dividiré en 2 partes
#3El único exception posible sería un ValueError



def menu():                           #Menú sencillo, sólo imprime las opciones
    print("""**** Calculator ****
1. Sum
2. Subtraction
3. Multiplication
4. Division
5. Clear 
6. Exit""")


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
    while True:           #Es un ciclo para que el usuario tenga derecho a equivocarse y lo resuelva con break o continue
        try:
            current_number = float(input("Enter the number for starting the operation: "))   #Primero necesito el número actual
            break         #Aquí cierro el ciclo                                                  
        except ValueError as error:
            print(f"Error! You must enter a valid number: {error}")
            continue
    
    while True:          #Es otro ciclo para resolver las dos opciones no matemáticas y dar cierre al programa
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
            break                        #Aquí cierro el ciclo                                                              
        elif option < 1 or option > 6:
            print("Error! Invalid option")
        else:                            #Aquí se resuelven las opciones matemáticas
            current_number = operation(option, current_number)


if __name__ == "__main__":
    calculator()