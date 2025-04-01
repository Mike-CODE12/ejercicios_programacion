#Variables mutables necesarias:
list_of_students=[]                     #Guardará toda la información de los estudiantes             Option2
list_of_average_grade_per_student=[]    #Esta lista es para ordenarla y sacar el top3                Option3
top_3=[]                                #Guardará el top 3                                           Option3
list_for_the_group_average_grade=[]     #Guardará todas las notas en una lista para luego sumarlas   Option4

group_average_grade=0  #Es una variable inmutable, pero funciona porque yo estoy realizando una nueva asignación en una función

#Option1: Reúno la información (Deberá validar que las notas ingresadas sean validas (números de 0 a 100) y seguir pidiéndola hasta que sea valida.)
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
    #Este ciclo lo utilizo para la creación de 3 listas diferentes
    for counter in range(number_of_students):   
        #Toda la información por estudiante   
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
        #Información de la nota promedio de cada estudiante
        dictionary_of_average_grade["Student"]=dictionary_of_student["Name"]
        dictionary_of_average_grade["Average_grade"]=dictionary_of_student["Average_grade_of_student"]
        list_of_average_grade_per_student.append(dictionary_of_average_grade)
        #Reuniendo las notas sin nombres para luego poderlas sumar (Necesito que sea una lista, para que sea mutable)
        list_for_the_group_average_grade.append(dictionary_of_student["Average_grade_of_student"])

#Option2:
def view_information_of_students():
    if len(list_of_students)>=1:
        print(list_of_students) 
    else:
        print("You need to enter information for at least 1 student to view information of students")

#Option3: Obtengo el top3
def get_top_3():
    if len(list_of_average_grade_per_student)<3:
        print("You need to enter information for at least 3 students to get the top 3")
    else:
    #Aquí obtengo la lista de notas promedio por estudiante en orden descendente para luego sacar el top 3 (Ordeno la lista de estudiantes)
        sorted_list_of_average_grade_per_student = sorted(list_of_average_grade_per_student, key=lambda x: x["Average_grade"], reverse=True)#Averigua como funciona esto
    #Aquí debo sacar una lista con el top 3
        for top in range(3):         #Que pasa si hay menos de 3?  Aqui tengo que meterlo en una condicion
            top_3.append(sorted_list_of_average_grade_per_student[top])
    #Aquí necesito sacar el key y value de cada uno de los diccionarios
        for student in top_3:        #student entrara siendo cada uno de los diccionarios
            print(f"{student['Student']} {student['Average_grade']}") #Aquí especifico el key que quiero imprimir

#Option4: Este otro ciclo lo utilizo para sacar e imprimir el promedio entre todas las notas   
def get_group_average_grade():
    group_average_grade=0
    if len(list_for_the_group_average_grade)<1:
        print("You need to enter information for at least 1 student to get the group average grade")
    else:
        for index in range(len(list_for_the_group_average_grade)):   
            group_average_grade=list_for_the_group_average_grade[index]+group_average_grade
        group_average_grade=group_average_grade/(index+1)        
        print(group_average_grade)
