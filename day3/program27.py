


#Program to check if a number is Prime
import math
 
input_number = int(input('Enter a number to check if it is Prime: '))
 
prime = True # Assume the number is Prime
for i in range(2, math.ceil(math.sqrt(input_number)+1)):
    if input_number % i == 0: # if N is divisible by any number other than 2 and itself
        prime = False
        break # break the loop
if prime:
    print(f'{input_number} is Prime number')

    
    count = 0
    for num in range(2, input_number + 1):
        # Check if num is prime
        is_prime = True
        if num <= 1:
            is_prime = False
        else:
            for i in range(2, math.ceil(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
        
        if is_prime:
            count += 1
    
    print(f'{input_number} is the {count}th prime number')
else:
    print(f'{input_number} is not a Prime number')






