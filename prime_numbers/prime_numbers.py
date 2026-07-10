"""
prime_numbers.py

This file is part of the "Cursor AI + Python: Intelligent Development with AI" course provided by Santander Open Academy.

Purpose:
    - Demonstrate how to implement an efficient algorithm for checking if a number is prime using the Python standard library.
    - Provide educational insight into primality testing and algorithmic thinking with code that is beginner-friendly and well-documented.

What is a prime number?
    - A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    - Examples of prime numbers: 2, 3, 5, 7, 11, 13, 17, ...

How does the implemented algorithm work?
    - First, handle edge cases: numbers less than 2 are not prime; 2 is the only even prime.
    - Exclude all other even numbers since they are not prime.
    - Use `math.isqrt(n)` to efficiently determine the integer square root of `n`, limiting trial division to possible divisors up to √n.
    - Only test odd divisors from 3 to √n (inclusive), since even divisors have already been excluded.
    - If any divisor evenly divides `n`, the function returns False (not prime); otherwise, the number is prime.

Why use math.isqrt()?
    - `math.isqrt(n)` computes the integer square root of `n` efficiently and safely for large numbers.
    - This allows us to only try divisors up to √n, a well-known mathematical optimization for primality testing.

Why test only odd divisors?
    - After excluding even numbers, all remaining candidates must be odd.
    - Testing only odd numbers in the loop reduces unnecessary checks and improves performance, while making the code more readable.

Educational purpose:
    - This file is intended for learners practicing Python basics and mathematical algorithms.
    - It features clear code, informative comments, and practical examples to reinforce concepts.

"""

import math

def is_prime(n):
    """
    Check if a given integer is a prime number.

    Args:
        n: The number to test for primality.

    Returns:
        True if n is prime, False otherwise.
    """

    if n < 2:
        return False  # Numbers less than 2 are not considered prime

    if n == 2:
        return True  # 2 is the only even prime number

    if n % 2 == 0:
        return False  # Exclude other even numbers

    # Only check odd divisors up to the integer square root of n
    limit = math.isqrt(n)

    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False  # Found a divisor, n is not prime

    return True  # No divisors found, n is prime

# Example usages and output to demonstrate the function:
print(is_prime(2))
print(is_prime(4))
print(is_prime(7))
print(is_prime(97))
print(is_prime(100))
print(is_prime(101))