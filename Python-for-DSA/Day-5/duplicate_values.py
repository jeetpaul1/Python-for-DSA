#Write a program to remove duplicates from a list and return a list of unique elements.



numbers = [1, 2, 3, 2, 4, 3, 5] #solution

# Removing duplicates
unique_numbers = list(set(numbers))

# Print results
print("Original List:", numbers)
print("List without duplicates:", unique_numbers)
