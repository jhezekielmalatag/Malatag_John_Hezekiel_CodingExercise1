# Ask user to enter a string
text = input("Enter a string: ")

# Convert the string to lower case
text = text.lower()

# Split the string into words
words = text.split()

# Sort the character in each words
result = []

for word in words:
    sorted_word = ''.join(sorted(word))
    result.append(sorted_word)
    
# Join the words with spaces
result = ' '.join(result)

# Display
print("Result:", result)