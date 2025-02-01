# Create a custom module named utilities.py with a function to calculate the factorial of a number. Import and use it in your main program.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
