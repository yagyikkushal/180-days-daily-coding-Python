# Write a Python program to select a string from a given list of strings with the most unique characters.

mylist = ['Green', 'Red', 'Orange', 'Yellow', '', 'White']

templist = []

for _ in mylist:
    templist.append(len(set(_)))

print(mylist[templist.index(max(templist))])