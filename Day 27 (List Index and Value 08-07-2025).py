# Write a Python program to find the indexes of numbers in a given list below a given threshold.

mylist = [0, 12, 4, 3, 49, 9, 1, 5, 3]
threshold = 10

indexlist = []

for index, value in enumerate(mylist):
    if value < threshold:
        indexlist.append(index)

print(indexlist)