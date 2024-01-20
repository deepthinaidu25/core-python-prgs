#78.	Write a Python program to print the Fibonacci series up to 100 by using the do-while statement

a,b=0,1
while True:
    print(a)
    a,b=b,a+b
    
    if a>100:
        break
   
