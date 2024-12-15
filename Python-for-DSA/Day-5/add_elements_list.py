#Write a program to create an empty list and add five numbers entered by the user.


numbers = []  #solution

# Add numbers to the list
for _ in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Print the list
print("The list is:", numbers)
