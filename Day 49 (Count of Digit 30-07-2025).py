# Write a Python program to find the sum of the numbers in a given list among the first k with more than 2 digits.

mylist = [114, 215, -117, 119, 14, 108, -9, 12, 76]
k = 5
reslist = 0

for _ in mylist[:k]:
    if (_%100) != _:
        reslist += _

print(reslist)