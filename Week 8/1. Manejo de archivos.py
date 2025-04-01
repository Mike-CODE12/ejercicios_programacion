def write_text_to_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

songs_text="""Moneytalks
Back In Black
Highway to Hell
You Shook Me All Night Long
Thunderstruck 
TNT 
Hell's Bells!"""

write_text_to_file("Songs.txt", songs_text)

songs_list = []

def open_and_read_file_returning(path):
    songs_list = []
    with open("Songs.txt","r", encoding='utf-8') as file2:
        song = file2.readline()
        while song:
            songs_list.append(song.strip())
            song = file2.readline()
    return songs_list

songs_list = open_and_read_file_returning("Songs.txt")
#Ya tengo el programa que lea nombres de canciones de un archivo (línea por línea) y los retorne en una lista


#Ya tengo la lista con las canciones

songs_list.sort()          #Ordeno los elementos de una lista
print(songs_list)          #Compruebo


def writelines_text_to_file(file_path, text_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        for song in text_list:
            file.write(song + '\n')         #+ '\n'
# Escribir cada canción en una nueva línea

writelines_text_to_file("file with sorted songs.txt", songs_list)
# Escribir las canciones ordenadas en el archivo "file with sorted songs.txt"


def open_and_read_file(path):
    with open(path, "r", encoding='utf-8') as file:
        reading= file.read()
        print(reading)

open_and_read_file("file with sorted songs.txt")