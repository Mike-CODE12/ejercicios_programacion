import csv

from Actions import Student, list_of_students_2

import os


def write_csv_file(file_path, iterable, header):                     
    with open(file_path, "w", encoding="utf-8", newline='') as file:  
        writer = csv.DictWriter(file, header)                         
        writer.writeheader()                                          
        writer.writerows(iterable)   


def read_csv_file(file_path):                                         
    with open(file_path, "r", encoding="utf-8") as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            student_2 = Student(
                name=row["Name"],
                section=row["Section"],
                spanish_grade=float(row["Spanish Grade"]),
                english_grade=float(row["English Grade"]),
                social_studies_grade=float(row["Social Studies Grade"]),
                science_grade=float(row["Science Grade"]),
                average_grade=float(row["Average Grade"]))
            list_of_students_2.append(student_2)
        for student_2 in list_of_students_2:
                print(f"Name: {student_2.name}, Section: {student_2.section}, Spanish Grade: {student_2.spanish_grade}, English Grade: {student_2.english_grade}, Social Studies Grade: {student_2.social_studies_grade}, Science Grade: {student_2.science_grade} Average Grade: {student_2.average_grade}, ")


def check_read_csv_file_exist(file_path):                              
    if os.path.exists(file_path):
        read_csv_file(file_path)
    else:
        print("CSV file does not exist")