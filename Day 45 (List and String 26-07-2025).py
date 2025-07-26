# Write a Python program to find a list of strings that have fewer total characters (including repetitions).

mylist = [['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]

reslist = []
templen = 0

for i in mylist:
    for j in i:
        templen += len(j)
    reslist.append(templen)
    templen = 0

print(mylist[reslist.index(min(reslist))])
