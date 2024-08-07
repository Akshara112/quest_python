input1 = input("Enter the first value: ")
input2 = input("Enter the second value: ")


def detect_type(value):
    try:
        # Attempt to convert the value to float
        float(value)
        return 'number'  # If successful, the value is a number
    except (ValueError, TypeError):
        return 'string'
    

def detect_and_process(value1, value2):   
    type1 = detect_type(value1)
    type2 = detect_type(value2)

    if type1 == 'number' and type2 == 'number':
        # Both values are numbers, perform addition
        return value1 + value2
    elif type1 == 'string' and type2 == 'string':
        # Both values are strings, perform concatenation
        return value1 + " " + value2
    elif type1 == 'number' and type2 == 'string':
        # First value is a number, second is a string
        return str(value1) + value2
    elif type1 == 'string' and type2 == 'number':
        # First value is a string, second is a number
        return value1 + str(value2)
    else:
        return "Error: Incompatible types for operation."


value1 = detect_type(input1)
value2 = detect_type(input2)


result = detect_and_process(value1, value2)
print(f"Result: {result}")