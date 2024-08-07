value1 = input("Enter the first value: ")
value2 = input("Enter the second value: ")
def process_data(value1, value2):
    if isinstance(value1, str) and isinstance(value2, str):
        
        return value1 + " " + value2
    elif isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
        
        return value1 + value2
    elif isinstance(value1, str) and isinstance(value2, (int, float)):
        
        try:
            
            return value1 + str(value2)
        except TypeError:
        
            return "Error: Cannot concatenate a string with a non-string value."
    elif isinstance(value1, (int, float)) and isinstance(value2, str):
    
        try:
            
            return str(value1) + value2
        except TypeError:
            
            return "Error: Cannot concatenate a non-string value with a string."
    else:
        return "Error: Incompatible types for operation."
    
result = process_data(value1, value2)
print(f"Result: {result}")








    
