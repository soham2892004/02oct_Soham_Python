words=["apple","banana","cherry","watermellon"]

longest_word=0

for word in words:
    if len(word) > longest_word:
        longest_word=len(word)
    print(longest_word)

