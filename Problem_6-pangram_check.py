# Ask user to enter a string
import string


text = input("Enter a string: ")

# Ask the string to lowercase and remove spaces
text = text.lower().replace(" ", "")

# Check if all alphabet letters are present
result = set(string.ascii_lowercase).issubset(set(text))

# Display
print("Result:", result)

