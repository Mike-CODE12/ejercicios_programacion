import csv


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
            print(row)


def check_read_csv_file_exist(file_path):                              
    if os.path.exists(file_path):
        read_csv_file(file_path)
    else:
        print("CSV file does not exist")