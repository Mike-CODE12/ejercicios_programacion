list_of_students=[]                    
list_of_average_grade_per_student=[]    
top_3=[]                                
list_for_the_group_average_grade=[]  
list_of_dictionaries=[]                        
list_of_students_2=[]

class Student():
    def __init__(self, name, section, spanish_grade, english_grade, social_studies_grade, science_grade, average_grade):
        self.name = name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_studies_grade = social_studies_grade
        self.science_grade = science_grade
        self.average_grade = average_grade    

    def convert_to_dict(self):
        return {
            "Name": self.name,
            "Section": self.section,
            "Spanish Grade": self.spanish_grade,
            "English Grade": self.english_grade,
            "Social Studies Grade": self.social_studies_grade,
            "Science Grade": self.science_grade,
            "Average Grade": self.average_grade}

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
        while True:
            name=input("Please enter the student's name: ")
            section=input("Please enter the student's section: ")
            try:
                spanish_grade=float(input("Please enter the student's Spanish grade: "))
                if spanish_grade<0:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                elif spanish_grade>100:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                else:
                    break
            except ValueError as ex:
                print(f"You did not enter a valid number:{ex}")
                continue 
        while True:  
            try:          
                english_grade=float(input("Please enter the student's English grade: "))
                if english_grade<0:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                elif english_grade>100:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                else:
                    break   
            except ValueError as ex:
                print(f"You did not enter a valid number:{ex}")
                continue  
        while True:  
            try:
                social_studies_grade=float(input("Please enter the student's Social Studies grade: "))
                if social_studies_grade<0:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                elif social_studies_grade>100:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                else:
                    break 
            except ValueError as ex:
                print(f"You did not enter a valid number:{ex}")
                continue   
        while True: 
            try:             
                science_grade=float(input("Please enter the student's Science grade: "))
                if science_grade<0:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                elif science_grade>100:
                    print("You did not enter a valid number for the grade. Please try again")
                    continue
                else:
                    break  
            except ValueError as ex:
                print(f"You did not enter a valid number:{ex}")
                continue   
        average_grade=float((spanish_grade+english_grade+social_studies_grade+science_grade)/4)

        student=Student(name, section, spanish_grade, english_grade, social_studies_grade, science_grade, average_grade)
        list_of_students.append(student)

        dictionary_of_average_grade["Student"]=name
        dictionary_of_average_grade["Average_grade"]=average_grade
        list_of_average_grade_per_student.append(dictionary_of_average_grade)

        list_for_the_group_average_grade.append(average_grade)
        list_of_dictionaries.append(student.convert_to_dict())

#Option2:     
def view_information_of_students():
    if len(list_of_students) >= 1:
        for student_object in list_of_students:
            print(f"Name: {student_object.name}, Section: {student_object.section}, "
                f"Spanish Grade: {student_object.spanish_grade}, English Grade: {student_object.english_grade}, "
                f"Social Studies Grade: {student_object.social_studies_grade}, Science Grade: {student_object.science_grade}, "
                f"Average Grade: {student_object.average_grade}")
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