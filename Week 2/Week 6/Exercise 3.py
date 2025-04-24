#3. Cree una función que retorne la suma de todos los números de una lista.
    #1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    #2. [4, 6, 2, 29] → 41


def sum_of_numbers_on_a_list(parameter_1):
    sum_of_list = 0
    for index in range(0, len(parameter_1)):
        sum_of_list = parameter_1[index] + sum_of_list
    return sum_of_list


sum_of_numbers_on_a_list([4, 6, 2, 29])