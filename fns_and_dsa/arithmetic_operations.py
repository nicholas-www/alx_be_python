
def perform_operation(num1, num2, operation):
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    operation = input("Enter the operation (add, subtract, multiply, divide): ")

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return 'Cannot divide by zero.'
        return num1 / num2

