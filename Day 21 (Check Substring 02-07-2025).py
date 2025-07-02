# Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.

list_of_strings = ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']


if list_of_strings[-2] in list_of_strings[-1]: #Learnt about how to check substring in a sting by "in" keyword.
    print("True")
else:
    print("False")