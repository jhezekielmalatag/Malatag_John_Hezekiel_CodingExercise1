# Ask user to enter a string
text = input("Enter a string: ")

# Ask user for the character to replace
curr_char = input("Enter the character to replace: ")

# Ask user for the new character
new_char = input("Enter the new character: ")

# Replace all occurrences
result = text.replace(curr_char, new_char)

# Display
print("Result:", result)