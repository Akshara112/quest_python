#Print X shape made up of stars of n lines
n = int(input('Enter the number of lines: '))

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:      # Print '*' at the positions of the diagonals
            print('*', end='')
        else:
            print(' ', end='')
    print()
