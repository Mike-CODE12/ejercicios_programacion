import io  
import contextlib 

from my_module_week_6.exercise_7 import is_prime, list_of_primes


def test_is_prime_with_prime_number():
    # Arrange
    input_number = 7
    expected_output = True
    # Act
    result = is_prime(input_number)
    # Assert
    assert result == expected_output


def test_is_prime_without_prime_number():
    # Arrange
    input_number = 9
    expected_output = False
    # Act
    result = is_prime(input_number)
    # Assert
    assert result == expected_output


def test_is_prime_with_number_less_than_2():
    # Arrange
    input_number  = 1
    expected_output = False
    # Act
    result = is_prime(input_number)
    # Assert
    assert result == expected_output


def test_list_of_primes_with_mixed_numbers():
    # Arrange
    input_list = [1, 4, 6, 7, 13, 9, 67]
    expected_output = "[7, 13, 67]"
    #Act
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        list_of_primes(input_list)
    actual_output = captured_output.getvalue().strip()
    # Assert
    assert actual_output == expected_output

def test_list_of_primes_with_all_primes():
    # Arrange
    input_list = [2, 3, 5, 7, 11]
    expected_output = "[2, 3, 5, 7, 11]"
    #Act
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        list_of_primes(input_list)
    actual_output = captured_output.getvalue().strip()
    # Assert
    assert actual_output == expected_output


def test_list_of_primes_with_no_primes():
    # Arrange
    input_list = [0, 1, 4, 6, 8, 9]
    expected_output = "[]"
    #Act
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        list_of_primes(input_list)
    actual_output = captured_output.getvalue().strip()
    # Assert
    assert actual_output == expected_output