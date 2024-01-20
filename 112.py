#112.	Write a Python program to find the sum of the even numbers up to 100

even_numbers = []

for i in range(2, 101, 2):
    even_numbers.append(i)


even_sum = sum(even_numbers)


print(f"The sum of even numbers up to 100 is: {even_sum}")
         
