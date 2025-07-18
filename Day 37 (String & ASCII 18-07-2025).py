# Write a Python program to compute the sum of the ASCII values of the upper-case characters in a given string.

string = 'JavaScript'
sum_of_uppercase = 0

for _ in string:
    if _.isupper():
        sum_of_uppercase += ord(_)

print(sum_of_uppercase)