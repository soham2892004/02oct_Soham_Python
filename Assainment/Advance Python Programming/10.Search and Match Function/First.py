import re

# Define the string to search
text = "The quick brown fox jumps over the lazy dog"

# Define the word to search for
word = "fox"

# Use re.search() to find the word in the string
match = re.search(r'\b{}\b'.format(word), text)

# Check if a match was found
if match:
    print("Word found:", match.group())
else:
    print("Word not found")
