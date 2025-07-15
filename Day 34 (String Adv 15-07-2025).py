# Write a Python program to split a given string (s) into strings if there is a space in s, otherwise split on commas if there is a comma, otherwise return the list of lowercase letters in odd order (order of a = 0, b = 1, etc.).

import re

s = input("Enter: ")

parts = re.split(r"[, ]",s)
mylist = []

if len(parts)>1:
    print(parts)
else:
    for _ in s:
        if s.index(_)%2 != 0:
            mylist.append(_)
    print(mylist)

