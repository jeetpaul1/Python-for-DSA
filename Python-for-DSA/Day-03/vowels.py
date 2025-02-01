#Write a program to count the number of vowels in a given string.


text = input("Enter a string: ") #solution

# Count vowels
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1

# Print result
print("Number of vowels in the string:", count)
