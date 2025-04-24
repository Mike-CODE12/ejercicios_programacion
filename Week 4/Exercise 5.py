grade_counter = 1
number_of_passed_grades = 0
number_of_failed_grades = 0
average_of_passed_grades = 0
average_of_failed_grades = 0
total_average_of_grades = 0
total_of_grades = int(input("Enter number of grades "))
while (grade_counter <= total_of_grades):
    current_grade = int(input(f'Enter grade number {grade_counter} '))
    if (current_grade < 70) :
        number_of_failed_grades =  number_of_failed_grades + 1
        average_of_failed_grades = average_of_failed_grades + current_grade
    else :
        number_of_passed_grades = number_of_passed_grades + 1
        average_of_passed_grades = average_of_passed_grades + current_grade
    total_average_of_grades = total_average_of_grades + current_grade    
    grade_counter = grade_counter + 1     
total_average_of_grades = total_average_of_grades / total_of_grades
if (number_of_failed_grades == 0) :
    print("Student has no failed grades, therefore there is no average of failed grades")
else :
    average_of_failed_grades = average_of_failed_grades / number_of_failed_grades
    print(f'Student has this number of failed grades: {number_of_failed_grades}')
    print(f'This is the average of failed grades: {average_of_failed_grades}')
if (number_of_passed_grades == 0) :
    print("Student has no passed grades, therefore there is no average of passed grades")
else :
    average_of_passed_grades = average_of_passed_grades / number_of_passed_grades
    print(f'Student has this number of passed grades: {number_of_passed_grades}')
    print(f'This is the average of passed grades: {average_of_passed_grades}')
print(f'This is the total average of grades: {total_average_of_grades}')