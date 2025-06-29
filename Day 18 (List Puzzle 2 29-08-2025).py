# Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.

mylist = []
count = 0
flag = 0
values_inside_list = int(input("Enter the number of integer values in the list: "))

for _ in range(values_inside_list):
    item = int(input(f"Enter the {_ + 1} value: "))
    if _ == 4:
        flag = item
    mylist.append(item)

for _ in mylist:
    if _ == flag:
        count = count + 1

if len(mylist) == 8 and count == 3:
    print("True")
else:
    print("False")