#72.	Write a Python program to print the Fibonacci series upto 100by using the while statement
#0,1,1,2,3,5,8,13,21 …
a,b=0,1
while a<=100:
    print(a)
    a,b=b,a+b
