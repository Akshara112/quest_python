#Print a hollow square of n lines
n = int(input('Enter the number of lines: '))

for i in range(n):
    for j in range(n):
        # Print '*' for the border
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            # Print space for the hollow part
            print(" ", end="")
    # Move to the next line after printing one row
    print()
