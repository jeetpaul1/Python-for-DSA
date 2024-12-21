#Write a Python program to perform a linear search on a list of integers and return all the indices where the target value appears. If the target does not exist, return an appropriate message.


def linear_search_all_indices(lst, target):  #solution
    """
    Perform a linear search to find all indices of the target in the list.

    Args:
        lst (list): The list of integers.
        target (int): The value to search for.

    Returns:
        list or str: A list of indices where the target is found, 
                     or a message if the target is not in the list.
    """
    indices = []
    for i in range(len(lst)):
        if lst[i] == target:
            indices.append(i)
    
    if indices:
        return indices
    else:
        return f"The target {target} is not in the list."

# Example usage
numbers = [5, 3, 7, 3, 9, 3, 1]
target_value = 3

result = linear_search_all_indices(numbers, target_value)
print(f"Indices of target {target_value}:", result)
