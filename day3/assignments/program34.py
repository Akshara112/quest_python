#to find the smallest and largest elements in the list
def find_min_max(numbers):

    smallest = min(numbers)
    largest = max(numbers)
    print(f"Smallest element: {smallest}")
    print(f"Largest element: {largest}")

# Input from user
numbers_list = input("Enter the list of numbers separated by spaces: ")
numbers = list(map(int, numbers_list.split())) 
find_min_max(numbers)
    




