my_tuple = ('apple', 50, 'fruit')
temp_list = list(my_tuple)
temp_list[1] = 60  
my_tuple = tuple(temp_list)
print("Modified tuple:", my_tuple)
