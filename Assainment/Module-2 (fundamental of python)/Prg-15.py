#initialise string and substring  and passed string values for both
string = "i am soham ,i learn python fundamental"
substring = "soham"

#initialise count and index variables and passed value 0 for both
count = 0
index = 0

while True:
  #find substring value in string variable
  index = string.find(substring, index)
  #if index value is equal to -1 so stop execution and execution to out of loop
  if index == -1:
    break
  count += 1
  index += len(substring)

#displayed result
print("Occurrences of substring:", count)