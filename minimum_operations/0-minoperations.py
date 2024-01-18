#!/usr/bin/python3
"""Minimum operations."""

def minOperations(n):

 """
    Calculate the fewest number of operations needed to achieve exactly n 'H' characters in a text file.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations needed.

    Note:
        If n is impossible to achieve, the function returns 0.
    """

    if n == 1:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0

# Example usage:
n = 50
result = minOperations(n)
print(result)
