# Program to display the Fibonacci sequence 

number_terms = int(input("enter the number of terms"))

number1, number2 = 0, 1
count = 0

# check if the number of terms is valid
if number_terms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif number_terms == 1:
   print("Fibonacci sequence upto",number_terms,":")
   print(number1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < number_terms:
       print(number1)
       nth = number1 + number2
       
       number1 = number2
       number2 = nth
       count += 1