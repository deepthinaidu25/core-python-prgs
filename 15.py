
principal, rate, time = map(float, input("Enter principal, rate, and time (in years),and n (compounding frequency): ").split())


simple_interest = (principal * rate * time) / 100
compound_interest = principal * (1 + rate / n)**(n * time) - principal

print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)
