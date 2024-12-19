#Write a program to sort a list of numbers in ascending order using Bubble Sort.

def bubble_sort(numbers):  #solution
    n = len(numbers)
    for i in range(n):
        # Traverse through the list
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# List to be sorted
numbers = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(numbers)
print("Sorted List:", numbers)
