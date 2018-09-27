my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
my_list = list(my_tuple)
my_list.insert(0, my_tuple)
my_list = list(my_list[0]) + my_list[1:]
my_set = set(my_list)