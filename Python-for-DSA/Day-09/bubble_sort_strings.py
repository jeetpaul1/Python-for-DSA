#Use Bubble Sort to sort a list of strings in alphabetical order.


def bubble_sort_strings(strings): #solution
    n = len(strings)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare strings lexicographically
            if strings[j] > strings[j + 1]:
                strings[j], strings[j + 1] = strings[j + 1], strings[j]

# List of strings
strings = ["banana", "apple", "cherry", "date"]

bubble_sort_strings(strings)
print("Sorted Strings:", strings)
