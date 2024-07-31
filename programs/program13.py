#Program to count the number of Odd digits in a number
input_number = int(input('Enter a number to count the number of odd digits in it: '))

count_of_digits = 0
temp_number = input_number

while temp_number != 0:
    digit = temp_number % 10
    if digit % 2 != 0:  # Check if the digit is odd
        count_of_digits += 1
    temp_number = temp_number // 10

print(f'Number of odd digits in {input_number} is {count_of_digits}')
