#Write a program to remove duplicates from a list by converting it to a set.

# Defining a list with duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5] #solution

# Remove duplicates using a set
unique_numbers = set(numbers)

# Print results
print("Original List:", numbers)
print("List without duplicates:", list(unique_numbers))
