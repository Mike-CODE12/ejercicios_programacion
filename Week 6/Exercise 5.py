#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un parameter_1.
# 1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”


def counter_of_upper_cases_and_lower_cases(parameter_1):
    lower_cases = 0
    upper_cases = 0
    for letter in parameter_1:
        if letter.isupper():
            upper_cases = upper_cases+1
    for letter in parameter_1:
        if letter.islower():
            lower_cases = lower_cases+1
    print(f"There’s {upper_cases} upper cases and {lower_cases} lower cases")


counter_of_upper_cases_and_lower_cases("I diDn't Know thIs wAs poSSible")