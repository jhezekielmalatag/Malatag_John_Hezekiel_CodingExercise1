# Ask user to enter a string
text = input("Enter a string: ")

# Split the string into words
words = text.split()

# Reverse each word and swap its case
result = [word[::-1].swapcase() for word in words]

# Join the words with spaces
result_string = ' '.join(result)

# Display
print("Result:", result_string)

