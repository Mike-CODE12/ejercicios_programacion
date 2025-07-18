#2 Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

list_to_sort =[96, 58, 100, 65, 97, 40, 7]

def bubble_sort(parameter_1):
    for outer_index in range(len(parameter_1)-1, 0, -1):
        has_made_changes=False
        for index in range(len(parameter_1)-1, len(parameter_1)-1 - outer_index, -1):
            current_element, previous_element=parameter_1[index], parameter_1[index-1]
            print(f"Iteration {len(parameter_1) - outer_index}.{len(parameter_1) - index}. Current element: {current_element}, Previous element: {previous_element}")
            if current_element>previous_element:
                print("Current element is greater than the previous one. Swapping them")
                parameter_1[index], parameter_1[index-1]=previous_element, current_element
                has_made_changes=True
        if not has_made_changes:
            return
        
bubble_sort(list_to_sort)
print(list_to_sort)