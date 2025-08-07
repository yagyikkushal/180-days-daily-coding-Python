# Write a Python program to sort numbers based on strings.

string = 'nine eight seven six five four three two one'

word_to_number = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10
}

mylist = string.split(" ")
mylist2 = []

for _ in mylist:
    mylist2.append(word_to_number[_])

myset = set(mylist2)

mylist2 = list(myset)

for _ in mylist2:
    for key, value in word_to_number.items():
        if value == _:
            print(key, end=" ")