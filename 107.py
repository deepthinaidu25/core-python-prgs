#107.	 write a Python program to find the sum of the natural numbers  up to N
N=int(input("enter the value of N:"))
sum=0
for i in range (1,N+1):
    sum=sum+i
print("the sum is",sum)
