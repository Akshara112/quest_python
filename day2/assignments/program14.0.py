
number_of_lines = int(input('Enter number of lines of the Triangle: '))

for i in range(1, number_of_lines+1):
    
    print(' ' * (number_of_lines - i) + '*' * i)