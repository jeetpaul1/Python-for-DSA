#Use Selection Sort logic to find the k-smallest element in a list.


def find_k_smallest(numbers, k):  #solution
    n = len(numbers)
    for i in range(k):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers[k - 1]

# List and k value
numbers = [7, 10, 4, 3, 20, 15]
k = 3

k_smallest = find_k_smallest(numbers, k)
print(f"The {k}-smallest element is:", k_smallest)
