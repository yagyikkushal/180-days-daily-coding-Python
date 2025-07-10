# Write a Python program to find strings in a given list starting with a given prefix.

mylist = [('do', ('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]

key = mylist[0][0]
flag = 0
word = str()
res = []

for _ in mylist[0][1]:
    for iterate in _[:len(key)]:
        word += iterate

    if word == key:
        res.append(_)

    word = ""

print(res)