the_greatest_number = 0
ten_numbers_list = []
for index in range(10):
    number = int(input(f"Enter number {index+1}: "))
    ten_numbers_list.append(number)
    if the_greatest_number <= number:
        the_greatest_number = number
print(f"List of numbers:{ten_numbers_list}")
print(the_greatest_number) 

















