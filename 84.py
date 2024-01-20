#84.	Write a Python program to print the odd numbers from X to Y by using the for statement
X=int(input("enter the value of X:"))
Y=int(input("enter the value of Y:"))

for i in range(X,Y+1):
    if i % 2 != 0:
       print(i)
