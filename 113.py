#113.	Write a Python program to find the sum of the first 100 even numbers
first_100_even_numbers=[]
for i in range(2,201,2):
    first_100_even_numbers.append(i)
sum_first_100_even=sum( first_100_even_numbers)
print(f"the sum of first 100 even numbers is:{sum_first_100_even}")
