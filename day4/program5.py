name = 'Cambodia'
 
names = ['aizwal', 'imphal', 'shillong', 'agartala']
 
print(name)  # Print the original string
print(name.upper())  # Print the string in uppercase
print(name.count('a'))   # Print the count of the lowercase letter 'a' in the string
print(name.count('A'))   # Print the count of the uppercase letter 'A' in the string
print(name.upper().count('A')) #  Converts the string to uppercase, then counts and prints the number of occurrences of 'A'. In 'CAMBODIA', there are 2 occurrences.
print(name.upper().count('a')) #  Converts the string to uppercase, then counts and prints the number of occurrences of 'a'. Since it's now 'CAMBODIA', there are 0 occurrences of 'a'.
print(name.find('o'))  #  Finds and prints the index of the first occurrence of the substring 'o' in the string 'Cambodia'. The first 'o' is at index 4.
print(name.find('dia'))   #  Finds and prints the index of the first occurrence of the substring 'dia' in the string 'Cambodia'. 'dia' starts at index 5
print(name.find('xx')) #returns -1 because the string we are trying ,# Explanation: Attempts to find the index of the substring 'xx'. Since 'xx' does not exist in 'Cambodia', it returns -1 to indicate no match.



'''# Define the string
name = 'Cambodia'

# Define the list of names
names = ['aizwal', 'imphal', 'shillong', 'agartala']

# Print the original string
print(name)  # Output: 'Cambodia'
# Explanation: Displays the string 'Cambodia'.

# Print the string in uppercase
print(name.upper())  # Output: 'CAMBODIA'
# Explanation: Converts all characters in the string to uppercase and prints it.

# Print the count of the lowercase letter 'a' in the string
print(name.count('a'))  # Output: 2
# Explanation: Counts and prints the number of occurrences of the lowercase letter 'a' in the string 'Cambodia'. There are 2 occurrences.

# Print the count of the uppercase letter 'A' in the string
print(name.count('A'))  # Output: 1
# Explanation: Counts and prints the number of occurrences of the uppercase letter 'A' in the string 'Cambodia'. There is 1 occurrence.

# Print the count of the uppercase letter 'A' in the uppercase version of the string
print(name.upper().count('A'))  # Output: 2
# Explanation: Converts the string to uppercase, then counts and prints the number of occurrences of 'A'. In 'CAMBODIA', there are 2 occurrences.

# Print the count of the lowercase letter 'a' in the uppercase version of the string
print(name.upper().count('a'))  # Output: 0
# Explanation: Converts the string to uppercase, then counts and prints the number of occurrences of 'a'. Since it's now 'CAMBODIA', there are 0 occurrences of 'a'.

# Print the index of the first occurrence of the substring 'o'
print(name.find('o'))  # Output: 4
# Explanation: Finds and prints the index of the first occurrence of the substring 'o' in the string 'Cambodia'. The first 'o' is at index 4.

# Print the index of the first occurrence of the substring 'dia'
print(name.find('dia'))  # Output: 5
# Explanation: Finds and prints the index of the first occurrence of the substring 'dia' in the string 'Cambodia'. 'dia' starts at index 5.

# Print the index of the first occurrence of the substring 'xx'
print(name.find('xx'))  # Output: -1
# Explanation: Attempts to find the index of the substring 'xx'. Since 'xx' does not exist in 'Cambodia', it returns -1 to indicate no match.
'''