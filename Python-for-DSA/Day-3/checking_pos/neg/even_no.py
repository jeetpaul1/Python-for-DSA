#Write a program to print all even numbers between two given numbers.


start = int(input("Enter the start number: ")) #solution
end = int(input("Enter the end number: "))

# Printing even numbers
print("Even numbers between", start, "and", end, ":")
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, end=" ")


