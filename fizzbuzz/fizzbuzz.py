"""
Purpose:
Implements the classic FizzBuzz programming challenge.

The program iterates through the numbers from 1 to 50 and applies the
following rules:

- Print "Fizz" for multiples of 3.
- Print "Buzz" for multiples of 5.
- Print "FizzBuzz" for numbers divisible by both 3 and 5.
- Otherwise, print the number itself.

This project was developed during the
"Cursor AI + Python: Intelligent Development with AI"
course provided by Santander Open Academy.
"""

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)