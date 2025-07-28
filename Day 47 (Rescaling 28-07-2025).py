# Write a Python program to rescale and shift numbers in a given list, so that they cover the range [0, 1].

mylist = [13.0, 17.0, 17.0, 15.5, 2.94]

reslist = []

for _ in mylist:
    reslist.append((_-min(mylist))/(max(mylist)-min(mylist)))

print(reslist)