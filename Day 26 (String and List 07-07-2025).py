# Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into groups of perfectly matched parentheses without any whitespace.

mylist = []
input_parantheses = input("Enter the parentheses: ").strip()
new = input_parantheses.replace(" ", "")
tempstr = str()
flag1 = 0
flag2 = 0

# print(new)
for _ in new:
    if _ != ')':
        tempstr += _
        flag1 += 1
    else:
        tempstr += _
        flag2 += 1
        if flag1 == flag2:
            mylist.append(tempstr)
            tempstr = ""
            flag1 = 0
            flag2 = 0

print(mylist)