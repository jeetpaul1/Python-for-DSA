#Modify Selection Sort to count the number of comparisons performed during sorting.


def selection_sort_count(numbers):  #solution
    n = len(numbers)
    comparison_count = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparison_count += 1
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    print("Number of comparisons:", comparison_count)

# List to be sorted
numbers = [3, 1, 2, 4]

selection_sort_count(numbers)
