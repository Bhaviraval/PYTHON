tuples_list = [(), ('apple', 50), (), ('banana', 20), ('milk', 30)]

filtered_list = [tup for tup in tuples_list if tup]
print("List after removing empty tuples:", filtered_list)
