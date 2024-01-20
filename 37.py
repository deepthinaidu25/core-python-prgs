#37.	Write a Python program to print the odd numbers up to N
N=int(input("enter the value of N:"))
for N in range(1,N,2):
    print(N, end = ' ')
