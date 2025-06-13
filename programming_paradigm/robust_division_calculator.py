def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
    except ValueError:
        print('Error: Please enter numeric values only.')
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
    else:
        return f'The result of the division is {result}'
 