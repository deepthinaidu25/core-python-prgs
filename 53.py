#53.	Write a Python program to find an electricity bill by following the below conditions
#a.	If number of units<=100 then unit price=Rs.1.20ps
#b.	If number of units>100 and number of units<=400 then unit price=Rs.2.80ps
#c.	If number of units>400 then unit price=Rs.6.80ps
def calculate_electricity_bill(units):
    if units<=100:
       unit_price=1.20
    elif units>100 and units<=400:
       unit_price=2.80
    else:
       unit_price=6.80
    bill=units*unit_price
    return bill
units_consumed=int(input("enter the number of units consumed:"))
total_bill=calculate_electricity_bill(units_consumed)
print(f"the electricity bill is: Rs.{total_bill:.2f}")

