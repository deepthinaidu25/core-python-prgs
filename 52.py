#52.	Write a Python program to find an income tax by following the above program conditions using the slab system
def calculate_income_tax(income):
    if income <= 10000:
        tax = 0
    elif income > 10000 and income <= 40000:
        tax = 0.05 * (income - 10000)
    elif income > 40000 and income <= 100000:
        tax = (0.05 * 30000) + (0.10 * (income - 40000))
    else:
        tax = (0.05 * 30000) + (0.10 * 60000) + (0.15 * (income - 100000))
    
    return tax
income_amount = float(input("Enter the income amount: "))
tax_amount = calculate_income_tax(income_amount)
print(f"The income tax is: {tax_amount}")
