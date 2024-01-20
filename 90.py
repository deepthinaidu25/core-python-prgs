#90.	Write a Python program to print the Nth multiplication table up to 20
N=int(input("enter the value of N:"))
for i in range (1,21):
    print(f"{N}x{i}={N*i}")
