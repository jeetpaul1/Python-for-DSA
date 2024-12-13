#Write a program to calculate the factorial of a number using a for loop.


num = int(input("Enter a number: ")) #solution

# Calculate factorial
factorial = 1
for i in range(1, num + 1):
    factorial *= i

# Print result
print("Factorial of", num, "is", factorial)
