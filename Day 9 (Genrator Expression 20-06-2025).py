# Write a Python program that yields cubes from 1 to n and filters out cubes that are even before printing them.

#Using Generator Expression

n = int(input("Enter a number: "))

gen = (_**3 for _ in range(1,n+1) if _%2 != 0)

for _ in gen:
    print(_)

#Using Generator Function

n = int(input("Enter a number: "))


def cube_gen(nth):
    for _ in range(1, nth + 1):
        yield _ ** 3


gen = cube_gen(n)

for _ in gen:
    if _ % 2 != 0:
        print(_)
    else:
        continue