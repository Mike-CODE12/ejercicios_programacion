#4. Cree una función que le de la vuelta a un parameter_1 y lo retorne.


def spelling_string_in_reverse(parameter_1):
    for spelling in range(len(parameter_1)-1, -1, -1):
        result = f"{parameter_1[spelling]}"
        print(result, end="")

if __name__ == "__main__":
    spelling_string_in_reverse("Testing with a very large string to avoid any kind of problem. It's necessary to check that it is working properly.")