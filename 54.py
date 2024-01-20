#with slab system
def calculate_electricity_bill(units):
    if units <= 100:
        bill = units * 1.20
    elif units > 100 and units <= 400:
        bill = 100 * 1.20 + (units - 100) * 2.80
    else:
        bill = 100 * 1.20 + 300 * 2.80 + (units - 400) * 6.80
    
    return bill


units_consumed = int(input("Enter the number of units consumed: "))


total_bill = calculate_electricity_bill(units_consumed)
print(f"The electricity bill is: Rs. {total_bill:.2f}")
