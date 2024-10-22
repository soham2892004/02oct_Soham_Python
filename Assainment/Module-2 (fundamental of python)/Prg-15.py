string = "i am soham ,i learn python fundamental"
substring = "python"

count = 0
index = 0

while True:
  index = string.find(substring, index)
  if index == -1:
    break
  count += 1
  index += len(substring)

print("Occurrences of substring:", count)