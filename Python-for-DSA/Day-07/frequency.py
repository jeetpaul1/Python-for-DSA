#Write a program to count how many times each element appears in a list.

# Define a list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4] #solution

# Create a frequency dictionary
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

# Print frequency dictionary
print("Frequency of numbers:", frequency)
