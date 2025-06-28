#1.Manejo de CSVs
def list_with_dictionaries():    
    list_of_dictionaries=[]         
    for attempts in range(1, 3):    
        try:                      
            number_of_games=int(input("Enter the number of videogames:  "))  
            if attempts<2:
                break               
        except ValueError as ex:    
            print(f"You did not enter a number: {ex}")
            attempts=attempts+1  
            if attempts>2:        
                print("For this reason the program will be closed.")
                exit()  
    for number_of_dictionaries in range(number_of_games):          
        dictionary={}            
        dictionary["Name"]=input("Enter videogame's name: ")
        dictionary["Genre"]=input("Enter videogame's genre: ")
        dictionary["Developer"]=input("Enter videogame's developer: ")
        dictionary["ESBR Rating"]=input("Enter videogame's ESRB Rating: ")
        list_of_dictionaries.append(dictionary)
    return(list_of_dictionaries)    


keys= ("Name", "Genre", "Developer", "ESBR Rating")


import csv

def write_csv_file(file_path, iterable, header):                      
    with open(file_path, "w", encoding="utf-8", newline='') as file:  
        writer = csv.DictWriter(file, header)                         
        writer.writeheader()                                         
        writer.writerows(iterable)                                   

write_csv_file("Videogames.csv", list_with_dictionaries(), keys)