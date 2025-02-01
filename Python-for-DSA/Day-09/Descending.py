#Modify Bubble Sort to sort a list in descending order.


def bubble_sort_desc(numbers):  #solution
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap if the current element is smaller than the next
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# List to be sorted
numbers = [5, 1, 4, 2, 8]

bubble_sort_desc(numbers)
print("Sorted List in Descending Order:", numbers)
