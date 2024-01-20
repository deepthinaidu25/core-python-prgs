def print_custom_pyramid(rows):
    for i in range(1, rows + 1):
        # Printing the leading spaces for formatting
        print(" " * (rows - i) * 4, end="")
        
        # Printing the left half of the pyramid
        for j in range(1, i + 1):
            print(j, end=" ")
        
        # Printing the right half of the pyramid
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        
        print()

rows = 5  # You can adjust the number of rows

print("Custom Pyramid pattern:")
print_custom_pyramid(rows)
