name = str(input("Enter name "))
last_name = str(input("Enter last name "))
full_name = (f"{name} {last_name}")
age = int(input("Enter age "))
if (age < 2) :
    print(f"{full_name} is a baby")
elif (age < 6) :
    print(f"{full_name} is a child")
elif (age < 12) :
    print(f"{full_name} is a preteen")
elif (age < 18) : 
    print(f"{full_name} is a teenager")
elif (age < 30) :
    print(f"{full_name} is a young adult")
elif (age < 65) :
    print(f"{full_name} is an adult")
else :
    print(f"{full_name} is an older adult")  