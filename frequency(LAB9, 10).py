def frequency(s):
    """
    Compute the frequency of words in the given string.
    
    :param s: Input string
    :return: Dictionary with words as keys and their frequencies as values, sorted by words
    """
    words = s.split()  # Split string into words
    freq_dict = {}  # Initialize frequency dictionary
    
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1  # Count occurrences
    
    return dict(sorted(freq_dict.items()))  # Return sorted dictionary

# Example usage:
input_string = "apple banana apple orange banana apple"
result = frequency(input_string)
print(result)
