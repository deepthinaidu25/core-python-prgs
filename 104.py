#104.	Write a Python program to find smallest in the given 10 numbers
list1=[]
N=int(input("enter the  N numbers:"))
for N in range(1,11):
    
    ele=int(input("enter elements:"))
    list1.append(ele)
print("the smallest of the N numbers is:",min(list1))
