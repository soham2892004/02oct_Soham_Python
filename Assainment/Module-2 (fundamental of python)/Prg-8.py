#take input from user
value=input("enter letter in alphabet:")

#if value included in AEIOU or aeiou so it's a vowel
if value in "aeiouAEIOU":
    print(value,"is vowel")
#when if condition false so else part execute automatically
else:
    print(value,"is not vowel")


