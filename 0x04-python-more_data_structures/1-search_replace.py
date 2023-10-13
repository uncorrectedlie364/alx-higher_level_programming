#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Searches for a specific element in a list and replaces it with a given value.
    
    Args:
    - my_list: The list to be searched and modified.
    - search: The element to search for in the list.
    - replace: The value to replace the searched element with.
    
    Returns:
    - The modified list with the specified element replaced.
    """
    # Create a new list by applying a lambda function to each element of my_list
    # The lambda function checks if the element is equal to search, if so, it replaces it with replace
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    
    return new_list
