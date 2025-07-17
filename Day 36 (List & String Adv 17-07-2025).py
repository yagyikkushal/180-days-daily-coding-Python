# Write a Python program to check, for each string in a given list, whether the last character is an isolated letter or not. Return True otherwise False.


mylist = ['ca t', 'car', 'fea r', 'cente r']
reslist = []

for _ in mylist:
    if _[-2] == " ":
        reslist.append(True)
    else:
        reslist.append(False)

print(reslist)