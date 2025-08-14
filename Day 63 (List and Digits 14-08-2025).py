# Write a Python program to find the indices of two entries that show that the list is not in increasing order. If there are no violations (they are increasing), return an empty list.

mylist = [-3, -2, -3, 0, 2, 3, 4]
reslist = []

for _ in mylist[0:-1]:
    if _ >= mylist[mylist.index(_) + 1]:
        reslist.append(mylist.index(_))
        reslist.append(mylist.index(_) + 1)
        break

print(reslist)