
first_100_odd_numbers = []


for i in range(1, 200, 2):  
    first_100_odd_numbers.append(i)


sum_first_100_odd = sum(first_100_odd_numbers)


print(f"The sum of the first 100 odd numbers is: {sum_first_100_odd}")
