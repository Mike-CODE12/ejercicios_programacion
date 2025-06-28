# 2. Intente accesar a una variable definida dentro de una función desde afuera.
# Intente accesar a una variable global desde una función y cambiar su valor.


global_variable = 4


def local_variable():
    internal_variable_1 = 1
    internal_variable_2 = 2
    result = internal_variable_1 + internal_variable_2
    print(result)


local_variable()


def local_variable_2():
    global_variable = 10
    print(global_variable)


local_variable_2()


print(global_variable)
print(internal_variable_1)