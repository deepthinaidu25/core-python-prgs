#51.	Write a Python program to find an income tax by following the below conditions
#a.	If income<=10000 then tax=0%
#b.	If income>10000 and income<=40000 then tax=5%
#c.	If income>40000 and income<=100000 then tax=10%
#d.	If income>100000 then tax=15%
def calculate_income_tax(income):
    if income<=10000:
       tax=0
    elif income>10000 and income<=40000:
       tax=0.05*income
    elif income>40000 and income<=100000:
       tax=0.10*income
    else:
        tax=0.15*income
    return tax
income_amount=float(input("enter the income amount"))
tax_amaount=calculate_income_tax(income_amount)
print(f"the income tax is :{tax_amount}")

     
