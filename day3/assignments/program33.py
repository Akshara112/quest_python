# swap the adjacent numbers in a list
def swap_adjacent(numbers):
    for i in range(0, len(numbers) - 1, 2):
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    print(numbers)

# Input from the user
numbers_list = input("Enter the list of numbers separated by spaces: ")
numbers = list(map(int, numbers_list.split()))

# Check if the number of elements is even
if len(numbers) % 2 == 0:
    swap_adjacent(numbers)
else:
    print("Please enter an even number of elements for swapping.")

    