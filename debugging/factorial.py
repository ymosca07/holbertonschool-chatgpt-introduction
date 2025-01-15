#!/usr/bin/python3
import sys

def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: ./program_name <number>")
        
        # Convert the argument to an integer
        num = int(sys.argv[1])
        
        # Calculate and print the factorial
        f = factorial(num)
        print(f)
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

