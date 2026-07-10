"""
This file contains a collection of introductory Python exercises developed during the
"Cursor AI + Python: Intelligent Development with AI" course provided by Santander Open Academy.

Purpose:
    - Practice Python programming fundamentals through practical problems.
    - Demonstrate the use of list comprehensions for constructing and filtering lists.
    - Apply basic mathematical operations on sequences (square, sum, etc.).
    - Implement a simple prime number checking algorithm.
    - Reinforce programming concepts in an educational and beginner-friendly context.

Exercises implemented:
    1. Generate a list of squares of the first n natural numbers.
    2. Calculate the sum of the squares of even numbers from a provided list.
    3. Calculate the sum of the squares of odd numbers from a provided list.
    4. Determine if a number is prime (basic approach).
    5. Calculate the sum of the squares of prime numbers from a provided list.

Key Python concepts practiced:
    - List comprehensions
    - Control flow (loops and conditionals)
    - Mathematical calculations
    - Reusable functions with clear docstrings and parameters
    - Simple algorithmic thinking

This file is intended for educational purposes and helps beginners develop problem-solving skills using Python.
"""


def quadrados(n):
    """
    Generates a list containing the squares of the first n natural numbers.

    Args:
        n: The number of natural numbers to generate squares for.

    Returns:
        A list of squared values from 1 to n (inclusive).
    """
    return [i ** 2 for i in range(1, n + 1)]


print(quadrados(10))


def soma_quadrados_pares(lista):
    """
    Calculates the sum of the squares of even numbers in a given list.

    Args:
        lista: A list of integers.

    Returns:
        The sum of the squares of all even numbers in the list.
    """
    return sum([i ** 2 for i in lista if i % 2 == 0])


print(soma_quadrados_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def soma_quadrados_impares(lista):
    """
    Calculates the sum of the squares of odd numbers in a given list.

    Args:
        lista: A list of integers.

    Returns:
        The sum of the squares of all odd numbers in the list.
    """
    return sum([i ** 2 for i in lista if i % 2 != 0])


print(soma_quadrados_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def eh_primo(n):
    """
    Checks whether a given integer is a prime number.

    Args:
        n: The integer to check.

    Returns:
        True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def soma_quadrados_primos(lista):
    """
    Calculates the sum of the squares of prime numbers in a given list.

    Args:
        lista: A list of integers.

    Returns:
        The sum of the squares of all prime numbers in the list.
    """
    return sum([i ** 2 for i in lista if eh_primo(i)])


print(soma_quadrados_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))