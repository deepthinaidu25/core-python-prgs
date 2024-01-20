
def sum_of_first_N_even_numbers(N):
    
    first_N_even_numbers = []

   
    for i in range(2, 2 * N + 1, 2):
        first_N_even_numbers.append(i)

    sum_first_N_even = sum(first_N_even_numbers)

    return sum_first_N_even

N = int(input("Enter the value of N: "))

# Call the function and print the result
result = sum_of_first_N_even_numbers(N)
print(f"The sum of the first {N} even numbers is: {result}")
