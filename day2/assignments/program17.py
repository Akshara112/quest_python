#to find the second smallest digit in a number
number = int(input('Enter a number to find the smallest digit: '))
    # Initialize the largest digit variable to 9
smallest_digit = 9

while number > 0:
        # Get the last digit
        digit = number % 10
        
        # Update largest_digit if the current digit is greater
        if digit < smallest_digit:
            smallest_digit = digit
        
        # Remove the last digit
        number = number // 10
    
print(f'The smallest digit in is {smallest_digit}')