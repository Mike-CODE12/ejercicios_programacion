#1 Crea un bubble_sort por tu cuenta sin revisar el código de la lección.

list_to_sort =[96, 58, 100, 65, 97, 40, 7]

def bubble_sort(parameter_1):
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
            return
        
bubble_sort(list_to_sort)
print(list_to_sort)