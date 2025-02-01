#Write a program to check if a number is between 1 and 10 using logical operators.


num = int(input("Enter a number of your choice :")) #Solution

# Checking if number is b/n 1 and 10
result = (num > 1 and 
          num < 10)

print("Is the number between 1 and 10?", result)
