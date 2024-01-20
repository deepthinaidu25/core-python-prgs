#105.	Write a Python program to find smallest in the given N numbers
list1=[]
N=int(input("enter the 10 numbers:"))
for N in range(1,N+1):
    ele=int(input("enter elements:"))
    list1.append(ele)
print("the smallest of the 10 numbers is:",min(list1))
