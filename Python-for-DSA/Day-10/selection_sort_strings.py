#Use Selection Sort to sort a list of strings in alphabetical order.


def selection_sort_strings(strings):  #solution
    n = len(strings)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if strings[j] < strings[min_index]:
                min_index = j
        strings[i], strings[min_index] = strings[min_index], strings[i]

# List of strings
strings = ["banana", "apple", "cherry", "date"]

selection_sort_strings(strings)
print("Sorted Strings:", strings)
