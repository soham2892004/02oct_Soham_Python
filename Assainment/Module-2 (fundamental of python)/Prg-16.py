# initialise string variable sentence
sentence = "hello i am soham , i am learn python language"

#initialise words variable,and passed string split method
words = sentence.split()

#initialise empty dictionary which name is word_count
word_count = {}

#define for loop which is represent word is in words variable
for word in words:
  #check condition if word in word_count dictionary,so word_count=word_count+1
  if word in word_count:
    word_count[word] += 1
  #when upper loop condition check,it's condition false,so else part execute 
  else:
    word_count[word] = 1

#displayed word_count disctionary perfectly
print(word_count)