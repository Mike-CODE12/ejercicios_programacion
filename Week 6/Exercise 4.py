#4. Cree una función que le de la vuelta a un parameter_1 y lo retorne.


def spelling_string_in_reverse(parameter_1):
    for spelling in range(len(parameter_1)-1, -1, -1):
        result = f"{parameter_1[spelling]}"
        print(result)


spelling_string_in_reverse("Writing in reverse")