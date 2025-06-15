import io  
import contextlib 

from my_module_week_6.exercise_5 import counter_of_upper_cases_and_lower_cases

def test_counter_of_upper_cases_and_lower_cases_without_string():
    #Arrange
    input_string = "  "
    output_string = "There’s 0 upper cases and 0 lower cases\n"
    #Act
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        counter_of_upper_cases_and_lower_cases(input_string)
    actual_output = captured_output.getvalue()
    #Assert
    assert actual_output == output_string
    

def test_counter_of_upper_cases_and_lower_cases_with_numbers():
    #Arrange
    input_string = "12345678F9871237897d"
    output_string = "There’s 1 upper cases and 1 lower cases\n"
    #Act
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        counter_of_upper_cases_and_lower_cases(input_string)
    actual_output = captured_output.getvalue()
    #Assert
    assert actual_output == output_string


def test_counter_of_upper_cases_and_lower_cases_with_only_uppercase_letters():
    #Arrange
    input_string = "STRING WITH ONLY UPPER LETTERS"
    output_string = "There’s 26 upper cases and 0 lower cases\n"
    #Act
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        counter_of_upper_cases_and_lower_cases(input_string)
    actual_output = captured_output.getvalue()
    #Assert
    assert actual_output == output_string