#96.	Write a Python program to print the below pyramid


def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

rows = 5  

print("Number Pyramid pattern:")
print_number_pyramid(rows)
