
numbers= [string for string in input().split(' ')]
print(numbers)

# Number of rows for the matrix
number_of_rows =int(input('enter the no of rows'))

# Calculate the number of columns
number_of_cols = len(numbers) // number_of_rows

# Create the matrix
matrix = [numbers[i * number_of_cols:(i + 1) * number_of_cols] for i in range(number_of_rows)]

# Print the matrix row-wise
for row in matrix:
    for element in row:
        print(element, end=' ')  # Print each element followed by a space
    print() 
    