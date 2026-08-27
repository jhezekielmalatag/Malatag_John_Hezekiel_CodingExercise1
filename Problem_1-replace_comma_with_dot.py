# Program asks user to enter a string
text = input("Enter a string: ")

# Program replaces all dots with commas
result = text.replace('.', ',')
result = text.replace(',', '.')

# Display
print("Result:", result)