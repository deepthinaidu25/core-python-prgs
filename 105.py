#105.	Write a Python program to find smallest in the given N numbers
N=int(input("enter the  N numbers:"))
for N in range(1,N+1):
    
    ele=int(input("enter elements:"))
    list1.append(ele)
print("the smallest of the N numbers is:",min(list1))
