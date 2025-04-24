list_of_students=[]                    
list_of_average_grade_per_student=[]    
top_3=[]                                
list_for_the_group_average_grade=[]     

#Option1
def gather_information():
    while True:
        try:
            number_of_students=int(input("Please enter the number of students to record information: "))
            if number_of_students<0:
                ("You did not enter a valid number for the number of students. Please try again")
                continue
            else:
                break
        except ValueError as ex:
            print(f"You did not enter a valid number:{ex}")
        continue 

    for counter in range(number_of_students):   

        dictionary_of_average_grade={}
        dictionary_of_student={}
        dictionary_of_student["Name"]=input("Please enter the student's name: ")
        dictionary_of_student["Section"]=input("Please enter the student's section: ")
        while True:
            try:
                dictionary_of_student["Spanish_grade"]=float(input("Please enter the student's Spanish grade: "))
                if dictionary_of_student["Spanish_grade"]<0:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                elif dictionary_of_student["Spanish_grade"]>100:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                else:
                    break
            except ValueError as ex:
                print(f"You did not enter a valid number:{ex}")
                continue 
        while True:  
            try:          
                dictionary_of_student["English_grade"]=float(input("Please enter the student's English grade: "))
                if dictionary_of_student["English_grade"]<0:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                elif dictionary_of_student["English_grade"]>100:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                else:
                    break   
            except ValueError as ex:
                print(f"You did not enter a valid number:{ex}")
                continue  
        while True:  
            try:
                dictionary_of_student["Social_studies_grade"]=float(input("Please enter the student's Social Studies grade: "))
                if dictionary_of_student["Social_studies_grade"]<0:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                elif dictionary_of_student["Social_studies_grade"]>100:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                else:
                    break 
            except ValueError as ex:
                print(f"You did not enter a valid number:{ex}")
                continue   
        while True: 
            try:             
                dictionary_of_student["Science_grade"]=float(input("Please enter the student's Science grade: "))
                if dictionary_of_student["Science_grade"]<0:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                elif dictionary_of_student["Science_grade"]>100:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                else:
                    break  
            except ValueError as ex:
                print(f"You did not enter a valid number:{ex}")
                continue   
        dictionary_of_student["Average_grade_of_student"]=float((dictionary_of_student["Spanish_grade"]+dictionary_of_student["English_grade"]+dictionary_of_student["Social_studies_grade"]+dictionary_of_student["Science_grade"])/4)
        list_of_students.append(dictionary_of_student)

        dictionary_of_average_grade["Student"]=dictionary_of_student["Name"]
        dictionary_of_average_grade["Average_grade"]=dictionary_of_student["Average_grade_of_student"]
        list_of_average_grade_per_student.append(dictionary_of_average_grade)

        list_for_the_group_average_grade.append(dictionary_of_student["Average_grade_of_student"])

#Option2:
def view_information_of_students():
    if len(list_of_students)>=1:
        print(list_of_students) 
    else:
        print("You need to enter information for at least 1 student to view information of students")

#Option3
def get_top_3():
    if len(list_of_average_grade_per_student)<3:
        print("You need to enter information for at least 3 students to get the top 3")
    else:
        sorted_list_of_average_grade_per_student = sorted(list_of_average_grade_per_student, key=lambda x: x["Average_grade"], reverse=True)#Averigua como funciona esto
        for top in range(3):         
            top_3.append(sorted_list_of_average_grade_per_student[top])
        for student in top_3:        
            print(f"{student['Student']} {student['Average_grade']}") 

#Option4
def get_group_average_grade():
    group_average_grade=0
    if len(list_for_the_group_average_grade)<1:
        print("You need to enter information for at least 1 student to get the group average grade")
    else:
        for index in range(len(list_for_the_group_average_grade)):   
            group_average_grade=list_for_the_group_average_grade[index]+group_average_grade
        group_average_grade=group_average_grade/(index+1)        
        print(group_average_grade)
