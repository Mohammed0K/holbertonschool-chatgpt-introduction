#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <non-negative-integer>".format(sys.argv[0]))
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: argument must be an integer.")
        sys.exit(1)

    print(factorial(n))
