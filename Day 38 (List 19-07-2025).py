# Write a Python program to find the indices at which the numbers in the list drop.

mylist = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
reslist = []

for _ in range(1,len(mylist)):
    if mylist[_-1]>mylist[_]:
        reslist.append(_)

print(reslist)