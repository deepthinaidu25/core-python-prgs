#119.	Write a Python program to find the product of first N even numbers
def prod(N):
    product=1
    for i in range(2,N*2+1,2):
        product*=i
    return product
N=int(input("enter the value of N:"))
result=prod(N)
print(f"Product of first {N} even numbers: {result}")
 
