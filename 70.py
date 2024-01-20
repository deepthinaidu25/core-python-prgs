#70.	Write a Python program to print the below series up to 200by using the while statement
#1,3,6,10,12,15,19 …
num = 1
increment = 2
add = 2

while num <= 200:
    print(num, end=" ")
    if increment % 2 == 0:
        num += add
        add += 2
    else:
        num += increment
    increment += 1

