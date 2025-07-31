# Write a Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.

num = 123456789
k = 10
reslist = []
reslist1 = []
res = 1

while num != num % k:
    reslist.append(num % k)
    k *= 10

reslist.append(num)

k = 1

for _ in reslist:
    if reslist.index(_) == 0:
        reslist1.append(_)
        k *= 10
    else:
        reslist1.append((_ - reslist[reslist.index(_) - 1]) / k)
        k *= 10

for _ in reslist1:
    if _ % 2 != 0:
        res *= _

if res == 1:
    print(0)
else:
    print(int(res))