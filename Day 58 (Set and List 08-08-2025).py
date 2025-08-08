# Write a Python program to find the set of distinct characters in a given string, ignoring case.

string = 'Ignoring case'
myset = set()

for _ in string:
    myset.add(_.lower())

mylist = list(myset)

print(mylist)