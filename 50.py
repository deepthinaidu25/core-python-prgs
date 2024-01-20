#50.	Write a Python program to find a sales man commission by following the above program conditions using the slab systemS
def calculate_commission(sales):
    if sales <= 1000:
        commission_rate = 0.10
    elif 1000 < sales <= 5000:
        commission_rate = 0.15
    else:
        commission_rate = 0.20
    
    commission = commission_rate * sales
    return commission


sales_amount = float(input("Enter the sales amount: "))

commission_amount = calculate_commission(sales_amount)

print(f"The salesman's commission is: {commission_amount}")
