def contains_substring(main_string, substring):
    """Check if `substring` is in `main_string`."""
    return substring in main_string

N = int(input("Enter the number of strings: "))

main_list = [string for string in input("Enter strings separated by spaces: ").split()]


sub_list = [string for string in input("Enter strings separated by spaces: ").split()]

# Create the presence list
presence = [1 if contains_substring(main_list[i], sub_list[i]) else 0 for i in range(N)]

# Print the results
print("Presence list:", presence)
