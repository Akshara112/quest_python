# Open a file in write mode
with open('output.txt', 'w') as file:
    # Print to the file
    print("Hello, World!", file=file)

# Verify the content by reading the file
with open('output.txt', 'r') as file:
    content = file.read()
    print("File content:", content)
