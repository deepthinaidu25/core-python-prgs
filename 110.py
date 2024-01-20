#110.	Write a Python program to find the sum of the odd numbers up to N

def sum_of_odd_numbers(N):
   
    odd_sum = 0
    
   
    for num in range(1, N + 1, 2):
       
        odd_sum += num
    
    return odd_sum


N = int(input("Enter a value for N: "))


result = sum_of_odd_numbers(N)
print(f"The sum of odd numbers up to {N} is: {result}")
