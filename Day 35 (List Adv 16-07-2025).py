# Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.

mylist = [6, 5, 4, 3, 2, 1]

if mylist[1]>mylist[0]:
    for i in range(2,len(mylist)):
        if mylist[i]>mylist[i-1]:
            pass
        else:
            print("Not a monotonic sequence")
            break
    print("Increasing")
elif mylist[1]<mylist[0]:
    for i in range(2,len(mylist)):
        if mylist[i]<mylist[i-1]:
            pass
        else:
            print("Not a monotonic sequence")
            break
    print("Decreasing")
else:
    print("Not a monotonic sequence.")