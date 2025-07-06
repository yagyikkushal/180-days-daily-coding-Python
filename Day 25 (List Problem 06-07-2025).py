# Write a Python program to find a list of integers containing exactly four distinct values, such that no integer repeats twice consecutively among the first twenty entries.

mylist = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

myset = set(mylist)
tempset = list(myset)


def consecuitve_checker(mylist):
    if len(mylist) < 20:
        for _ in range(1, len(mylist)):
            if mylist[_] == mylist[_ - 1]:
                return False
                break
    else:
        for _ in range(1, 20):
            if mylist[_] == mylist[_ - 1]:
                return False
                break


if len(tempset) == 4 and consecuitve_checker(mylist) != False:
    print(True)
else:
    print(False)