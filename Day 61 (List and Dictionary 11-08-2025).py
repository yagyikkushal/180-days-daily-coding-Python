# Write a Python program to find all words in a given string with n consonants.

string = 'this is our time'

mylist = string.split(" ")
mydict = {}

def find_no_of_consonant(word):
    count = 0
    for _ in word:
        if _ in 'aeiou':
            continue
        else:
            count += 1

    return count

for i in mylist:
    if find_no_of_consonant(i) in mydict:
        mydict[find_no_of_consonant(i)].append(i)
    else:
        mydict[find_no_of_consonant(i)] = [i]

sorted_dict = dict(sorted(mydict.items(), reverse=True))

for key, value in sorted_dict.items():
    print(f"Number of consonants: {key}")
    print(f"Words in the said string with {key} consonants:")
    print(value)