# Ask user for a string
text = input("Enter a string: ")

# Count each character
counts = {}

for char in text:
    if char != " ":
        counts[char] = counts.get(char, 0) + 1
            
# Get the characters that appear more than one
repeated = []

for char in counts:
    if counts[char] > 1:
        repeated.append(char)
        
#Sort the repeated characters alphabetically
repeated.sort()

# Display
print(len(repeated))

if len(repeated) > 0:
    print(" ".join(repeated))
else:
    print("None")