rows = int(input('Enter number of rows of the Matrix: '))
columns = 3
 
matrix1 = []
for i in range(rows):
    print(f'Enter {columns} numbers of Row-{i+1}')
    row_numbers = [] # List that stores numbers of a specific row
    for j in range(columns): # To read numbers of a row
        row_numbers.append(int(input()))
    matrix1.append(row_numbers)
 
for row in matrix1:
    for number in row:
        print('%3s'%(number), end='')
    print()