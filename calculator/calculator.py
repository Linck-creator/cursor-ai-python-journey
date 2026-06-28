"""
To package this calculator script as a Windows executable using PyInstaller, follow these steps:

1. Install PyInstaller with pip (in your terminal or command prompt):
   pip install pyinstaller

2. Use PyInstaller to generate the executable from your script:
   pyinstaller --onefile calculator.py

3. The standalone .exe will be created in the 'dist' directory.

Below is the script, ready for use with PyInstaller.
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
            print(num1 + num2)
        elif operation == "-":
            print(num1 - num2)
        elif operation == "*":
            print(num1 * num2)
        elif operation == "/":
            # Handle division by zero
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(num1 / num2)
        else:
            # Handle invalid operation input
            print("Error: Invalid operation. Please enter one of +, -, *, /.")
            continue  # Skip to next loop iteration

if __name__ == "__main__":
    main()