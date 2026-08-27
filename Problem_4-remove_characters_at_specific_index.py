# Ask user to enter a string
text = input("Enter a string: ")

# Ask user for index of the character to remove
n = int(input("Enter the index: "))

# Check if the index is valid
if n >= 0 and n < len(text):
    result = text[:n] + text[n+1:]

else:
    result = text
    
# Display
print("Result:", result)
