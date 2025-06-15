import io 
import contextlib 

from my_module_week_6.exercise_4 import spelling_string_in_reverse

def test_spelling_string_in_reverse_with_upper_and_lower_letters():
    #Arrange
    input_string = "Testing WITH thIs STRING"
    output_string = "GNIRTS sIht HTIW gnitseT"
    #Act
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        spelling_string_in_reverse(input_string)
    actual_output = captured_output.getvalue()
    #Assert
    assert actual_output == output_string


def test_spelling_string_in_reverse_with_a_large_string():
    #Arrange
    input_string = "Testing with a very large string to avoid any kind of problem. It's necessary to check that it is working properly."
    output_string = ".ylreporp gnikrow si ti taht kcehc ot yrassecen s'tI .melborp fo dnik yna diova ot gnirts egral yrev a htiw gnitseT"
    #Act
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        spelling_string_in_reverse(input_string)
    actual_output = captured_output.getvalue()
    #Assert
    assert actual_output == output_string


def test_spelling_string_in_reverse_with_a_small_string():
    #Arrange
    input_string = "oh"
    output_string = "ho"
    #Act
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        spelling_string_in_reverse(input_string)
    actual_output = captured_output.getvalue()
    #Assert
    assert actual_output == output_string