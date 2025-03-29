def create_list(list1, list2):
    """
    Return the intersection of two lists.
    
    :param list1: First list
    :param list2: Second list
    :return: List containing common elements from both lists
    """
    return list(set(list1) & set(list2))  # Convert to sets and find intersection

# Example usage:
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

result = create_list(list_a, list_b)
print(result)
