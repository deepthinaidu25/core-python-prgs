#69.	Write a Python program to print the below series up to 200by using the while statement
#1,3,6,8,11,13,16,18 …
num=1
increment=2
counter=1
while num<=200:
    print(num)
    if counter%2==0:
        num+=2
    else:
        num+=1
        counter+=1
