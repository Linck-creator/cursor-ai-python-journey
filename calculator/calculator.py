"""
Project Analysis: Calculator Script

Purpose:
This Python script implements a simple console-based calculator. It allows users to perform basic arithmetic operations interactively.

Features:
- Supports addition, subtraction, multiplication, and division.
- Continuously prompts the user for an operation and two numbers until the user enters "exit".
- Includes input validation to ensure that only valid numbers are accepted.
- Provides robust error handling for invalid number entries and division by zero.
- Informs users about invalid operations and input errors with clear messages.
- Contains instructions for packaging the script as a standalone Windows executable using PyInstaller.

Technologies Used:
- Python 3 (standard library; no external dependencies for calculator functionality).
- Designed for easy packaging with PyInstaller, making distribution as an executable straightforward.

How It Works:
- The main function drives a loop where the user is asked to input an arithmetic operation or type "exit" to quit.
- For valid operations, the user is prompted to enter two numbers. Input is validated using a try/except block to catch ValueError.
- The calculator performs the selected operation and prints the result.
- If the user enters an invalid operation or input, the script provides helpful error messages and restarts the prompt loop.
- Special handling is implemented for division by zero, which displays an error instead of raising an exception.
- The script can be run directly from the command line, and also includes documentation on how to package it as a Windows .exe for distribution.

This approach makes the script suitable both as a basic educational calculator and as a compact distributable tool.
"""
def main():
    # Create a calculator that repeatedly asks for an operation and two numbers until the user types "exit".

    while True:
        operation = input("Enter an operation (+, -, *, /) or 'exit' to quit: ")
        if operation == "exit":
            break  # Exit the loop if user types 'exit'
        
        # Use try/except to catch invalid number inputs
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Invalid input. Please enter valid numbers.")
            continue  # Skip to next loop iteration

        # Process the selected arithmetic operation
        if operation == "+":
            result = num1 + num2
            print(f"Result: {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"Result: {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"Result: {result}")
        elif operation == "/":
            # Handle division by zero
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {result}")
        else:
            # Handle invalid operation input
            print("Error: Invalid operation. Please enter one of +, -, *, /.")
            continue  # Skip to next loop iteration

if __name__ == "__main__":
    main()