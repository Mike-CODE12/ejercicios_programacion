import os


from Data import write_csv_file, read_csv_file, check_read_csv_file_exist


from Actions import list_of_students, list_of_average_grade_per_student, top_3, list_for_the_group_average_grade, gather_information, view_information_of_students, get_top_3, get_group_average_grade


def print_menu():
    print("        ****** Grade Management ******        ")
    print("1. Enter information of students")
    print("2. View the information of all registered students")
    print("3. Check the top 3 students with the highest average grade")
    print("4. Check the average grade among all students")
    print("5. Export all current data to a CSV file")
    print("6. Import data from a CSV file")
    print("7. Exit")


def run_menu():
    while True:
        print_menu()
        while True:
            try:
                option=int(input("Please select an option: "))
                break
            except ValueError as ex:
                print(f"Please enter a valid option. Try again : {ex}")
                continue
        if option==1:
            gather_information()
        elif option==2:
            view_information_of_students()
        elif option==3:
            get_top_3()
        elif option==4:
            get_group_average_grade()
        elif option==5:
            if len(list_of_students)>=1:
                write_csv_file("Information_of_students.csv", list_of_students, list_of_students[0].keys())
            else:
                print("You need to enter information for at least 1 student to get a CSV file")
        elif option==6:  
            check_read_csv_file_exist("Information_of_students.csv")
        if option==7:
            print("Exiting")
            break
            exit()