#104.	Write a Python program to find smallest in the given 10 numbers
list1=[]

for N in range(1,11):
    
    ele=int(input("enter elements:"))
    list1.append(ele)
print("the smallest of the 10 numbers is:",min(list1))
