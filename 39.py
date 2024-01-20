#39.	Write a Python program to find biggest in the given two numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if  num1>num2:
    largest = num1
else:
    largest = num2

# Print the largest number
print("The largest number is:", largest)
