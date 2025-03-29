def convert(s):
    words = set(s.split())  
    sorted_words = sorted(words)  
    return " ".join(sorted_words)  

input_string = "apple banana orange apple mango banana"
result = convert(input_string)
print(result)
