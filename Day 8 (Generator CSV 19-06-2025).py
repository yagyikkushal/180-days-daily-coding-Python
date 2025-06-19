# Write a Python script that generates cubes using a generator and outputs the cubes in a single comma‐separated string.

#First_Way

n = int(input("Enter a value:"))

def cubes_gen(nth):
    for i in range(1,nth+1):
        yield i**3

gen = cubes_gen(n)

for j in range(1,n+1):
    if j == n:
        print(next(gen))
    else:
        print(next(gen),end = ",")

#Second_Way

# Write a Python script that generates cubes using a generator and outputs the cubes in a single comma‐separated string.

n = int(input("Enter a number: "))


def cube_gen(nth):
    for _ in range(1, nth + 1):
        yield _ ** 3


gen = cube_gen(n)

result = ",".join(str(next(gen)) for _ in range(1, n + 1))
print(result)
5