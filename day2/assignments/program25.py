#Print a hollow square of n lines with diagonal
n = int(input('Enter the number of lines: '))

for i in range(n):
    for j in range(n):
        # Check if the position is on the border or diagonal
        if (i == 0 or i == n - 1 or j == 0 or j == n - 1 or
            i == j or i + j == n - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
