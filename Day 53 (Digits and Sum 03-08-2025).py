# Write a Python program to sort the numbers in a given list by the sum of their digits.

mylist = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sortlist = []


def digitsinfo(number):
    k = 1
    digitlist = []
    reslist = []

    while True:
        if int(number / k) == 0:
            break
        else:
            digitlist.append(int(number / k))
            k *= 10

    for _ in digitlist[0:len(digitlist)]:
        if digitlist.index(_) == len(digitlist) - 1:
            reslist.append(_)
        else:
            reslist.append(_ - (digitlist[digitlist.index(_) + 1] * 10))

    return sum(reslist)


for _ in mylist:
    sortlist.append(digitsinfo(_))

print(sortlist)
