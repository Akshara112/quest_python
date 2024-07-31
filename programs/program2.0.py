#check if a no is a perfect square
import math
input_number=int(input("enter a number to check if its a perfect square"))
root_number=int(math.sqrt(input_number))
root_number_square=root_number*root_number
if root_number_square==input_number:
    print(f"{input_number} is prefect square")
else:
    print(f"{input_number}is not prefect square")
