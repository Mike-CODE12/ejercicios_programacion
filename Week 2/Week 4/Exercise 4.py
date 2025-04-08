the_greatest_one = -999999999
counter = 1
while (counter <= 3):
    number=int(input("Enter number: "))
    if (the_greatest_one < number):
        the_greatest_one = number
    else:
        the_greatest_one = the_greatest_one
    counter = counter + 1
print(f"The greatest number is {the_greatest_one}")