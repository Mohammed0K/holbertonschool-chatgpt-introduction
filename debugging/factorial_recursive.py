#!/usr/bin/python3
import sys

def factorial(n):
    """
    Compute the factorial of a non-negative integer.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of n (n!).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # Read the input number from command-line arguments
    f = factorial(int(sys.argv[1]))
    # Print the computed factorial
    print(f)

