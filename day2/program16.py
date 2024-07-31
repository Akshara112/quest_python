#to find the largest digit in a number
number = int(input('Enter a number to find the largest digit: '))
    # Initialize the largest digit variable to 0
largest_digit = 0

while number > 0:
        # Get the last digit
        digit = number % 10
        
        # Update largest_digit if the current digit is greater
        if digit > largest_digit:
            largest_digit = digit
        
        # Remove the last digit
        number = number // 10
    
print(f'The largest digit in is {largest_digit}')
