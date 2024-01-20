#47.	Write a Python program to find the given number is either even or odd
def Even_or_odd(num):
    if num%2==0:
       return "even"

    else:
       return "odd"
number=int(input("enter the number:"))
result=Even_or_odd(number)
print(f"the number {number} is {result}")
       
