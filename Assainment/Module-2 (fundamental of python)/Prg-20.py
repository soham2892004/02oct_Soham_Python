#initialise list variable ,that include fruits values
words=["apple","banana","cherry","watermellon"]

#initialise variable longest_word,ii's value passed 0
longest_word=0

for word in words:
    #check condition,if length of word is greater than variable Longest_word
    if len(word) > longest_word:
        longest_word=len(word)

#displayed variable value longest_word        
    print(longest_word)

