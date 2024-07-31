#Find sum of Even placed digits in a number
input_number = int(input('Enter a number to find the sum of even-placed digits in it: '))
temp_number = input_number

sum_even_placed_digits = 0
position = 1  # Initialize position counter

while temp_number != 0:
    remainder_digit = temp_number % 10  # Get the last digit
    temp_number = temp_number // 10     # Remove the last digit from temp_number
    
    # Check if the position is even
    if position % 2 == 0:
        sum_even_placed_digits += remainder_digit
    
    position += 1  # Move to the next position

print(f'Sum of even-placed digits in {input_number} is {sum_even_placed_digits}')
