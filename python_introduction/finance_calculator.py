income = float(input("What is your monthly income?"))
expenses = float(input("What is your monthly expenses?"))

savings = income - expenses

projected_savings = savings * 12 + (savings * 12 * 0.05)

print(f'Your monthly savings are ${savings}')
print(f'Projected savings after one year, with interest, is: ${projected_savings}')