#Modify Bubble Sort to count the number of swaps performed during sorting.


def bubble_sort_count(numbers): #solution
    n = len(numbers)
    swap_count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swap_count += 1
    print("Number of swaps:", swap_count)

# List to be sorted
numbers = [3, 2, 1]

bubble_sort_count(numbers)
