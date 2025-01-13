#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: ./factorial.py <non-negative integer>")
        num = int(sys.argv[1])
        result = factorial(num)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    except RecursionError:
        print("Error: Maximum recursion depth exceeded. Input is too large.")
