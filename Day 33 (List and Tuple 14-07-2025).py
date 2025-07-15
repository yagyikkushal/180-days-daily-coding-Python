mylist = [([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]), 19]
mylist2 = []

key = mylist[1]

for i in mylist[0]:
    for j, k in enumerate(i):
        if k == key:
            mylist2.append([mylist[0].index(i), j])
        else:
            continue

print(mylist2)
