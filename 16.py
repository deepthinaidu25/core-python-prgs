#Python program to calculate simple interest
 
P = float(input("Enter the principal amount : "))
 
N = float(input("Enter the number of years : "))
 
R = float(input("Enter the rate of interest : "))

SI = (P * N * R)/100
CI =  P * (pow((1 + R / 100), N)) 
print("Simple interest :",SI)
print("Compound interest :",CI)


