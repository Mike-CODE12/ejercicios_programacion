#Archivo separado por tabulaciones en vez de por comas.


def list_with_dictionaries():    #Primera parte
    list_of_dictionaries=[]         #Creo la lista de diccionarios, que el usuario va a llenar, por eso empieza vacía
    for attempts in range(1, 3):    #Quiero que el usuario tenga derecho a equivocarse una vez
        try:                        #Sé que puede ocurrir un ValueError
            number_of_games=int(input("Enter the number of videogames:  "))   #El ValueError sería un string como int
            if attempts<2:
                break               #Si el usuario no se equivoca, este pequeño ciclo de revisión se romperá para continuar con el programa
        except ValueError as ex:    #Si se equivoca ocurrirá lo siguiente
            print(f"You did not enter a number: {ex}")
            attempts=attempts+1  
            if attempts>2:          #Si se vuelve a equivocar, cierre el programa
                print("For this reason the program will be closed.")
                exit()  
    for number_of_dictionaries in range(number_of_games):          #Aquí inicio el ciclo de creación de diccionarios
        dictionary={}              #Creo el diccionario, que el usuario va a llenar, por eso empieza vacío
        dictionary["Name"]=input("Enter videogame's name: ")
        dictionary["Genre"]=input("Enter videogame's genre: ")
        dictionary["Developer"]=input("Enter videogame's developer: ")
        dictionary["ESBR Rating"]=input("Enter videogame's ESRB Rating: ")
        list_of_dictionaries.append(dictionary)
    return(list_of_dictionaries)    #Guardo la lista de diccionarios creada


keys= ("Name", "Genre", "Developer", "ESBR Rating")


import csv
#Segunda parte: crear un archivo cvs con esa lista de diccionarios
def write_csv_file(file_path, iterable, header):                      #Creo una función para escribir el archivo cvs
    with open(file_path, "w", encoding="utf-8", newline='') as file:  # Agrego el parámetro newline='' para evitar que se agregue una línea vacía extra al escribir el archivo
        writer = csv.DictWriter(file, header, delimiter='\t')                         #Uso el objeto DictWriter para especificar los fieldnames para las columnas
        writer.writeheader()                                          #Escribo los encabezados
        writer.writerows(iterable)                                    #Escribo las filas

write_csv_file("Videogamestab.csv", list_with_dictionaries(), keys)