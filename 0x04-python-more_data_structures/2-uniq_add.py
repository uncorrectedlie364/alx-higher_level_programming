#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Calculates the sum of unique elements in a list.
    
    Args:
    - my_list: The list of numbers.
    
    Returns:
    - The sum of unique elements in the list.
    """
    # Convert the list to a set to remove duplicates and get unique elements
    uniq_list = set(my_list)
    
    # Initialize a variable to store the sum
    num = 0
    
    # Iterate over the unique elements and add them to the sum
    for i in uniq_list:
        num += i
    
    return num
