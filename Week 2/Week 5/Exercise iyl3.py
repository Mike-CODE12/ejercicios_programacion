my_list = [10, 20, 30, 40, 50, 60, 70]
if (len(my_list)>1):
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)