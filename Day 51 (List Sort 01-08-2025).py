# Write a Python program to find the largest k numbers from a given list of numbers.

mylist = [1, 2, 3, 4, 5, 5, 3, 6, 2]
reslist = []

k = 5

sorted_list = sorted(mylist, reverse=True)

for _ in sorted_list[:k]:
    reslist.append(_)

print(reslist)