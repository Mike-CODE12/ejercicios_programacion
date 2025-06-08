#1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.


def first_print():
    print("Calling")
    second_print()


def second_print():
    print("to the second function")


first_print()