list1 = []  
for i in range(1, 11):
    ele = int(input(f"Enter element {i}: "))
    list1.append(ele)

# Find and print the largest element in the list
print("Largest element is:", max(list1))
