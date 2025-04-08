dictionary = {}
list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]
for index in range(len(list_b)) :
    dictionary[list_a[index]] = list_b[index]
print(dictionary)