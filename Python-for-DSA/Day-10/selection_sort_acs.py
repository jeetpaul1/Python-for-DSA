#Write a program to sort a list of numbers in ascending order using Selection Sort.

def selection_sort(numbers): #solution
    n = len(numbers)
    for i in range(n):
        # Find the minimum element in the remaining unsorted part
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        # Swap the found minimum with the first element of the unsorted part
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# List to be sorted
numbers = [64, 25, 12, 22, 11]

selection_sort(numbers)
print("Sorted List:", numbers)
