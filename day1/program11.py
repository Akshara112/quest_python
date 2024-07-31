# Program to count the number of  odd digits in a number
 
input_number = int(input('Enter a number to count number of digits in it: '))
 
count_of_digits = 0
temp_number = input_number
 
while temp_number != 0:
    temp_number = temp_number // 10
    while temp_number%2==0:
        count_of_digits += 1
 
print(f'Number of digits in {input_number} is {count_of_digits}')