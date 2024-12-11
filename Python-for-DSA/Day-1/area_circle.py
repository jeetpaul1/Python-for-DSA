#Write a program to calculate the area of a circle given its radius.

# Import the math module for pi

import math #solution
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2) #calculating the area of circle - π * r²
print("Area of the circle:", area)