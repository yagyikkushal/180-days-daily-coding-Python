# Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.

mylist = []
flag_19 = 0
flag_5 = 0
value_to_input = input("Enter number of values you want to input in a list: ")

for _ in range(int(value_to_input)):
    item = int(input(f"Enter {_ + 1} value :"))
    mylist.append(item)

for item in mylist:
    if item == 19:
        flag_19 = flag_19 + 1
    elif item == 5:
        flag_5 = flag_5 + 1
    else:
        continue

print(f"\n{mylist}\n")

if flag_19 == 2 and flag_5 > 2:
    print("True")
else:
    print("False")