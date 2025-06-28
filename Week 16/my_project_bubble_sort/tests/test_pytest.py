#1. Cree los siguientes unit tests para el algoritmo `bubble_sort`:
# 1. Funciona con una lista pequeña.

import pytest
from my_module.bubble_sort import bubble_sort

def test_bubble_sort_returns_result_small_list():
    input_list = [96, 58, 100]
    expected_output = [58, 96, 100]

    result = bubble_sort(input_list)

    assert result == expected_output


#Funciona con una lista grande (de más de 100 elementos.)

def test_bubble_sort_returns_result_large_list():
    input_list = [23, 101, 45, 102, 12, 103, 87, 104, 3, 105, 67, 106, 55, 107, 2, 108, 99, 109, 38, 110,
    61, 111, 9, 112, 44, 113, 71, 114, 18, 115, 53, 116, 7, 117, 80, 118, 29, 119, 6, 120,
    82, 121, 1, 122, 48, 123, 15, 124, 58, 125, 11, 126, 64, 127, 4, 128, 74, 129, 25, 130,
    37, 131, 8, 132, 69, 133, 14, 134, 47, 135, 10, 136, 72, 137, 21, 138, 59, 139, 5, 140,
    90, 141, 16, 142, 42, 143, 31, 144, 66, 145, 20, 146, 85, 147, 28, 148, 13, 149, 62, 150,
    19, 151, 76, 152, 34, 153, 49, 154, 17, 155, 54, 156, 26, 157, 68, 158, 22, 159, 60, 160,
    30, 161, 46, 162, 27, 163, 24, 164, 35, 165, 32, 166, 39, 167, 36, 168, 50, 169, 41, 170,
    43, 171, 40, 172, 52, 173, 33, 174, 56, 175, 57, 176]
    
    expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
    39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 
    58, 59, 60, 61, 62, 64, 66, 67, 68, 69, 71, 72, 74, 76, 80, 82, 85, 87, 
    90, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 
    114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 
    129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 
    144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 
    159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 
    174, 175, 176]

    result = bubble_sort(input_list)

    assert result == expected_output


#Funciona con una lista vacía.
def test_bubble_sort_empty_list_returns_result_empty_list():
    input_list = []
    expected_output = []

    result = bubble_sort(input_list)

    assert result == expected_output


#No funciona con parámetros que no sean una lista.

@pytest.mark.parametrize("invalid_input", [
    "una cadena",
    123,
    3.14,
    None,
    {'a': 1},
    (1, 2, 3),
    True
])

def test_bubble_sort_another_type_returns_raise(invalid_input):
    with pytest.raises(TypeError):
        bubble_sort(invalid_input)