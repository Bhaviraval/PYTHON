def is_dict_empty(d):
    if not d:
        return True
    else:
        return False

dict1 = {}
dict2 = {'key': 'value'}

print(f"dict1 is empty: {is_dict_empty(dict1) }")
print(f"dict2 is empty: {is_dict_empty(dict2) }")
