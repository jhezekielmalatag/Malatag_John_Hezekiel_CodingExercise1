# Ask the user to enter a string
text = input("Enter a string: ")

# Ask the user to enter a prefix
prefix = input("Enter a prefix: ")

# Check if the string starts with the prefix
result = text.startswith(prefix)

# Display the result
print("Result:", result)