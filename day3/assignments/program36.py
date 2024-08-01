#to remove the negative numbers from a list
def remove_negative_numbers(numbers):
    # Using list comprehension to filter out negative numbers
    positive_numbers = [num for num in numbers if num >= 0]
    return positive_numbers

# Input from user
numbers_str = input("Enter the list of numbers separated by spaces: ")
numbers = list(map(int, numbers_str.split())) 

# Remove negative numbers
filtered_numbers = remove_negative_numbers(numbers)

print("List after removing negative numbers:", filtered_numbers)
