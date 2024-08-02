
def contains_substring(string, substring):
    """Check if `substring` is in `string`."""
    return substring in string


strings = [string for string in input("Enter strings separated by spaces: ").split()]

print(strings)



# Read the substring to search for
X = input("Enter the substring to search for: ")

# Initialize counter
count = 0

# Count how many of the `N` strings contain the substring `X`
for string in strings:
    if contains_substring(string, X):
        count += 1

# Print the number of strings that contain the substring `X`
print(f"Number of strings containing '{X}': {count}")




