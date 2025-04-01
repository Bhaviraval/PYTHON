my_tuple = ('apple', 50, 'fruit')

temp_list = list(my_tuple)
del temp_list[1]  
my_tuple = tuple(temp_list)

print("Tuple after deleting an element:", my_tuple)
