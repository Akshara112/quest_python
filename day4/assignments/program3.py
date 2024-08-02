def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]


data = [string for string in input("Enter strings separated by spaces: ").split()]

print(data)

# Initialize counter
palindrome_count = 0

# Count the number of palindromes
for string in data:
    if is_palindrome(string):
        palindrome_count += 1

# Print the number of palindromes
print(f"Number of palindromes: {palindrome_count}")
