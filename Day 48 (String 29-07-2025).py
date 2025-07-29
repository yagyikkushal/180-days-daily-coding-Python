# Write a Python program to find the positions of all uppercase vowels (not counting Y) in even indices of a given string.

string = 'AEIOUYW'
reslist = []

for _ in string:
    if string.index(_) % 2 == 0 and (_ == 'A' or _ == 'E' or _ == 'I' or _ == 'O' or _ == 'U'):
        reslist.append(string.index(_))

print(reslist)