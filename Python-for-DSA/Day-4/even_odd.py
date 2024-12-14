#Check If a Number is Even or Odd


def is_even(num):  #solution
    if num % 2 == 0:
        return True
    else:
        return False

# Using the function
number = 7
if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
