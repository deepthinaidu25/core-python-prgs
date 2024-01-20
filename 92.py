#92.	Write a Python program to print the first 5 multiplication tables, an each table up to 10
def print_multiplication_table(number, limit):
    print(f"Multiplication table of {number}:")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")
    print()
for i in range(1, 6):
    print_multiplication_table(i, 10)
