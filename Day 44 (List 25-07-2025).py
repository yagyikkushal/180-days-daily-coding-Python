# Write a Python program to find the indices of two numbers that sum to 0 in a given list of numbers.

mylist = [1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
reslist = []

for _ in mylist:
    if _ < 0:
        if -1 * _ in mylist:
            reslist.append(mylist.index(_))
            reslist.append(mylist.index(-_))

print(reslist)