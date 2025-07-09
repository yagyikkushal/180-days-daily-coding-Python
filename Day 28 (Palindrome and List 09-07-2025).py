# Write a Python program to check whether the given strings are palindromes or not. Return True otherwise False.


mylist = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
reslist = []

for _ in mylist:
    for s, u in zip(_, reversed(_)):
        if s == u:
            flag = 0
        else:
            flag = 1
            break

    if flag == 0:
        reslist.append("True")
    else:
        reslist.append("False")

print(reslist)