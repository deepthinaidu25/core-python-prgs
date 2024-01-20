#100.	Write a Python program to find the product of 10 numbers
N = int(input("Enter the value of N: "))
N = int(N)
prod = 1
for num in range(1, N + 1, 1):
    prod = prod * num
print("Product of first", N, "numbers is:", prod)
