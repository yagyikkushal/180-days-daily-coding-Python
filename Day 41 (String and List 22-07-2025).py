# Write a Python program to find the largest number where commas or periods are decimal points.


mylist = ['100', '102,1', '101.1']

for _ in mylist:
    if ',' in _:
        mylist[mylist.index(_)] = _.replace(',', '.')

print(max(mylist))