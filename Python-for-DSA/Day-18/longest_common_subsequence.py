#Write a Python program to find the length of the Longest Common Subsequence (LCS) of two strings. Also, reconstruct the LCS string.


def longest_common_subsequence(X, Y):  #solution
    """
    Find the Longest Common Subsequence (LCS) of two strings.

    Args:
        X (str): First string.
        Y (str): Second string.

    Returns:
        tuple: Length of the LCS and the LCS string.
    """
    m, n = len(X), len(Y)
    # Create a 2D DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], ''.join(reversed(lcs))

# Example usage
X = "AGGTAB"
Y = "GXTXAYB"
length, lcs = longest_common_subsequence(X, Y)
print(f"Length of LCS: {length}")
print(f"LCS: {lcs}")
