
def perform_operation(num1, num2, operation):
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    operation = input("Choose the operation (+, -, *, /): ")

    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 != 0:
                return num1 / num2
            return 'Cannot divide by zero.'