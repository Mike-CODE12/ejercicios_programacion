#6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
# 1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
# 2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”


def sort_words(parameter_1):
    list_of_words = parameter_1.split('-')
    list_of_words.sort()
    list_of_words = '-'.join(list_of_words)
    print(list_of_words)


sort_words("python-variable-funcion-computadora-monitor")