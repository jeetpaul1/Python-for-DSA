#Modify Bubble Sort to terminate early if the list is already sorted.


def optimized_bubble_sort(numbers): #solution
    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        # Break out if no swaps occurred
        if not swapped:
            break

# List to be sorted
numbers = [1, 2, 3, 4, 5]

optimized_bubble_sort(numbers)
print("Optimized Bubble Sort Result:", numbers)
