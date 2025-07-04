# Write a Python program to check a given list of integers where the sum of the first i integers is i.

mylist = [1, 1, 1, 1, 1, 1]


if sum(mylist) == len(mylist):
    print("True")
else:
    print("False")