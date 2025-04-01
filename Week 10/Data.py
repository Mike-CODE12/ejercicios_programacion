import csv


import os


def write_csv_file(file_path, iterable, header):                      #Creo una función para escribir el archivo cvs
    with open(file_path, "w", encoding="utf-8", newline='') as file:  #Agrego el parámetro newline='' para evitar que se agregue una línea vacía extra al escribir el archivo
        writer = csv.DictWriter(file, header)                         #Uso el objeto DictWriter para especificar los fieldnames para las columnas
        writer.writeheader()                                          #Escribo los encabezados
        writer.writerows(iterable)   


def read_csv_file(file_path):                                         #Función para leer o importar archivo
    with open(file_path, "r", encoding="utf-8") as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            print(row)


def check_read_csv_file_exist(file_path):                              #Función para revisar si el archivo existe antes de leerlo
    if os.path.exists(file_path):
        read_csv_file(file_path)
    else:
        print("CSV file does not exist")