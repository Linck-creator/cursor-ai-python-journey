# Create a calculator that repeatedly asks for an operation and two numbers until the user types "exit".

# Changed 'while true:' to 'while True:' (Python is case-sensitive)
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