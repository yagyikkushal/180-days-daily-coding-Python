string = 'Python'
ns = ''

for _ in string:
    if _.isupper():
        ns += _.lower()
    else:
        ns += _.upper()

print(ns)