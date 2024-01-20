#49.	Write a Python program to find a salesman commission by following the below conditions without using the slab system.
#a.	If sales<=1000 then commission=10%
#b.	If sales>1000 & sales<=5000 then commission = 15%
#c.	If sales>5000 then commission = 20%

def calculate_commission(sales):

    if sales<=1000:
       commission=0.10*sales
    elif 1000< sales <=5000:
       commission=0.15*sales
    else:
       commission=0.20*sales
    return commission
sales_amount=(float(input("eneter the sales amount")))
commission_amount = calculate_commission(sales_amount)             
print(f"The salesman's commission is: {commission_amount}")
