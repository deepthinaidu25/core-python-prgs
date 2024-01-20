#76.	Write a Python program to print the natural numbers up to N by using the do-while statement
N=int(input("enter the value of N:"))
num=1
while True:
    if num<=N:
        print(num)
        num+=1
        if num>N:
            break
