#Write a Python program to implement Binary Search iteratively. Return the index of the target if found, or a message if the target does not exist.


def binary_search_iterative(lst, target):  #solution
    """
    Perform a binary search to find the index of the target in a sorted list.

    Args:
        lst (list): The sorted list of integers.
        target (int): The value to search for.

    Returns:
        int or str: The index of the target if found, or a message if not found.
    """
    left, right = 0, len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if lst[mid] == target:
            return mid  # Target found
        elif lst[mid] < target:
            left = mid + 1  # Narrow search to the right half
        else:
            right = mid - 1  # Narrow search to the left half
    
    return f"The target {target} is not in the list."

# Example usage
sorted_numbers = [2, 4, 6, 8, 10, 12, 14]
target_value = 10

result = binary_search_iterative(sorted_numbers, target_value)
print(f"Index of target {target_value}:", result)
