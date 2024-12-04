#create UDF function Check_Palindrome
def Check_Palindrome(string):

  # Convert the string to lowercase and remove spaces
  string = string.lower().replace(" ", "")

  # Compare the string with its reversed version
  return string == string[::-1]

#initialise word variable 
word1="racecar"
word2="soham"

print(Check_Palindrome(word1))
print(Check_Palindrome(word2))

