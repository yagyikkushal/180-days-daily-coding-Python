# Write a Python program to create a string consisting of non-negative integers up to n inclusive.

value = int(input("Enter a number: "))

for _ in range(value+1):
    print(_, end= " ")