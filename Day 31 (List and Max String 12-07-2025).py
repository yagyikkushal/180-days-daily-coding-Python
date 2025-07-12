# Write a Python program to find the longest string in a given list of strings.

givenlist = ['cat', 'car', 'fear', 'center']
length = 0
lengthlist = []

for _ in givenlist:
    lengthlist.append(len(_))

string = max(lengthlist)

index_num = lengthlist.index(string)

print(givenlist[index_num])
