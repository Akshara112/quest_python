#to find the smallest and largest string from list of n strings
def find_smallest_and_largest(strings):
    # Initialize variables
    smallest = largest = strings[0]
    
    for x in strings:
        if len(x) < len(smallest):
            smallest = x
        if len(x) > len(largest):
            largest = x
    
    print(f"Smallest string by size: '{smallest}'")
    print(f"Largest string by size: '{largest}'")

# Input from the user
strings_list = input("Enter the list of strings separated by spaces: ")
strings = strings_list.split()

find_smallest_and_largest(strings)
