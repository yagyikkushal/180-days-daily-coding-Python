# Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.


temp = str()
mylist1 = []
mylist2 = []

value = input("Enter the string: ")

for _ in value:
    if _ == " ":
        if value[value.index(_)-1] == ",":
            continue
        else:
            mylist1.append(temp.strip())
            mylist2.append(" ")
            temp = ""
    elif _ == ",":
        mylist1.append(temp.strip())
        mylist2.append(", ")
        temp = ""
    elif _ == value[-1]:
        temp += _
        mylist1.append(temp.strip())
    else:
        temp += _

mylist3 = [mylist1,mylist2]
print(mylist3)


