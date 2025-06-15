import io  
import contextlib 

from my_module_week_6.exercise_6 import sort_words


def test_sort_words_():
    import io
import contextlib

def test_sort_words_with_mixed_case_words():
    # Arrange
    input_string = "zebra-Apple-mango-Banana"
    output_string = "Apple-Banana-mango-zebra"
    # Act
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        sort_words(input_string)
    actual_output = captured_output.getvalue().strip()
    # Assert
    assert actual_output == output_string

def test_sort_words_with_sorted_words():
    # Arrange
    input_string = "apple-ball-cat-dog"
    output_string = "apple-ball-cat-dog"
    # Act
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        sort_words(input_string)
    actual_output = captured_output.getvalue().strip()
    # Assert
    assert actual_output == output_string