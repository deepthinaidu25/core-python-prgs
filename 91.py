#91.	Write a Python program to print the Nth multiplication table up to x1
def print_multiplication_table(n, x1):
    print(f"Multiplication table of {n} up to {x1}:")
    for i in range(1, x1 + 1):
        print(f"{n} x {i} = {n * i}")
number = int(input("Enter the number for the multiplication table: "))
limit = int(input(f"Print the {number} multiplication table up to: "))

print_multiplication_table(number, limit)
