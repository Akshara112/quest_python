numbers = [23, 7, 19, 41, 29, 3, 47]
 
print('Max number = ', max(numbers))
print('Min number = ', min(numbers))
print('Number of elements = ', len(numbers))
print('Sorted numbers = ', sorted(numbers)) #stored in a temp list original list is maintained
print('Numbers = ', numbers)
numbers.sort()
print('Numbers = ', numbers)
