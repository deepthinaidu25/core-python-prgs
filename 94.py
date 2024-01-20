#95.	Write a Python program to print the prime numbers up to 100
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print("Prime numbers up to 100:")
for num in range(2, 101):
    if is_prime(num):
        print(num)
