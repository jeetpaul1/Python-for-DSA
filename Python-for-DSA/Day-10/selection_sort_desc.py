#Modify Selection Sort to sort a list in descending order.


def selection_sort_desc(numbers): #solution
    n = len(numbers)
    for i in range(n):
        # Find the maximum element in the remaining unsorted part
        max_index = i
        for j in range(i + 1, n):
            if numbers[j] > numbers[max_index]:
                max_index = j
        # Swap the found maximum with the first element of the unsorted part
        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

# List to be sorted
numbers = [20, 12, 10, 15, 2]

selection_sort_desc(numbers)
print("Sorted List in Descending Order:", numbers)
