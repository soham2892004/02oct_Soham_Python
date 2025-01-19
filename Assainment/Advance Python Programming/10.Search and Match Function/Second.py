import re

# Define the string to search
text = "Hello world, welcome to Python programming."

# Define the word to match
word = "Hello"

# Use re.match() to check if the word matches the beginning of the string
match = re.match(r'{}'.format(word), text)

# Check if a match was found
if match:
    print("Word found at the beginning of the string:", match.group())
else:
    print("Word not found at the beginning of the string")
