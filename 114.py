#114.	Write a Python program to find the sum of the even numbers up to N
a=[]
N=int(input("enter the value of N:"))
   
for i in range(2,N+1,2):
    a.append(i)
even_sum=sum(a)
print(f"the sum of even numbers upto {N} is:{even_sum}")
    
