from my_module_week_6.exercise_3 import sum_of_numbers_on_a_list

def test_sum_of_numbers_on_a_list_with_positive_numbers():
    #Arrange
    input_list = [1, 2, 3, 4, 5]
    expected_output = 15
    #Act
    result = sum_of_numbers_on_a_list(input_list)
    #Assert
    assert result == expected_output


def test_sum_of_numbers_on_a_list_with_negative_numbers():
    #Arrange    
    input_list = [-1, -2, -3]
    expected_output = -6
    #Act
    result=sum_of_numbers_on_a_list(input_list)
    #Assert
    assert result == expected_output


def test_sum_of_numbers_on_a_list_with_mixed_numbers():
    #Arrange    
    input_list = [10, -5, 20, -10]
    expected_output = 15
    #Act
    result=sum_of_numbers_on_a_list(input_list)
    #Assert
    assert result == expected_output