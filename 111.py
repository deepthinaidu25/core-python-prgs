def sum_of_first_N_odd_numbers(N):
   
    odd_sum = 0
    
   
    for i in range(1, 2 * N + 1, 2):
        odd_sum += i
    
    return odd_sum


N = int(input("Enter the value of N: "))


result = sum_of_first_N_odd_numbers(N)
print(f"The sum of the first {N} odd numbers is: {result}")
