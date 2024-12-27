# Write a Python program to compute the n-th Fibonacci number using both memoization and tabulation approaches. Additionally, return the series up to the n-th number.


# Fibonacci using Memoization (Top-Down)
def fibonacci_memoization(n, memo={}):   #solution
    """
    Compute the nth Fibonacci number using memoization.

    Args:
        n (int): The index of the Fibonacci number to compute.
        memo (dict): A dictionary to store computed Fibonacci numbers.

    Returns:
        int: The nth Fibonacci number.
    """
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

# Fibonacci using Tabulation (Bottom-Up)
def fibonacci_tabulation(n):
    """
    Compute the nth Fibonacci number using tabulation.

    Args:
        n (int): The index of the Fibonacci number to compute.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Generate the Fibonacci series up to nth number
def fibonacci_series(n):
    """
    Generate the Fibonacci series up to the nth number.

    Args:
        n (int): The number of terms in the Fibonacci series.

    Returns:
        list: A list containing the Fibonacci series up to nth number.
    """
    series = [0, 1]
    for i in range(2, n):
        series.append(series[i - 1] + series[i - 2])
    return series[:n]

# Example usage
n = 10
print(f"Fibonacci Series (First {n} terms): {fibonacci_series(n)}")
print(f"{n}th Fibonacci (Memoization): {fibonacci_memoization(n)}")
print(f"{n}th Fibonacci (Tabulation): {fibonacci_tabulation(n)}")
