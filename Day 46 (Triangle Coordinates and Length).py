# Write a Python program to find the coordinates of a triangle with given side lengths.

mylist = [5, 6, 7]

reslist = []

reslist.append([0.0,0.0])
reslist.append([mylist[0],0.0])

a = (((mylist[2]**2) + (mylist[0]**2) - (mylist[1]**2))/(2*mylist[0]))
b = ((mylist[2]**2) - (a**2))**0.5

reslist.append([a,b])

print(reslist)