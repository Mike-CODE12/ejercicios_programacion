#1 Crea un bubble_sort por tu cuenta sin revisar el código de la lección.

def bubble_sort(parameter_1):
    if not isinstance(parameter_1, list):
        raise TypeError("The entered parameter must be a list")
    for outer_index in range(0, len(parameter_1)-1):
        has_made_changes=False
        for index in range(0, len(parameter_1)-1-outer_index):
            current_element, next_element=parameter_1[index], parameter_1[index+1]
            print(f"Iteration {outer_index+1}.{index+1}. Current element: {current_element}, Next element: {next_element}")
            if current_element>next_element:
                print("Current element is greater than the next. Swapping them")
                parameter_1[index], parameter_1[index+1]=next_element, current_element
                has_made_changes=True
        if not has_made_changes:
            return parameter_1
    return parameter_1

if __name__ == "__main__":
    lista="w"
    lista_2=[8,5,9,2]
    bubble_sort(lista_2)