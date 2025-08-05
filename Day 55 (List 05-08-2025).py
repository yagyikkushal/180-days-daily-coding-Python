# Write a Python program to determine which triples sum to zero from a given list of lists.

mylist = [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]
reslist = []

for i in mylist:
    if sum(i) == 0:
        reslist.append(True)
    else:
        reslist.append(False)

print(reslist)