sentence = "hello i am soham , i am learn python language"
words = sentence.split()
word_count = {}

for word in words:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

print(word_count)