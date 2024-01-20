#103.	Write a Python program to find biggest in the given N numbers
list1=[]
N=int(input("enter the number of element in list:"))
for i in range(1,N+1):
    ele=int(input("enter element:"))
    list1.append(ele)
print("largest element is :",max(list1))
