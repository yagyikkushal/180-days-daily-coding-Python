# Write a Python program to create a list whose ith element is the maximum of the first i elements from an input list.

mylist = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]

reslist = []
temp = mylist[0]

for _ in mylist:
    if temp < _:
        reslist.append(_)
        temp = _
    else:
        reslist.append(temp)

print(reslist)