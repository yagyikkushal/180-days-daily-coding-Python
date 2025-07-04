# Write a Python program that creates a generator function that yields cubes of numbers from 1 to n. Accept n from the user.

def cubes_generator(n):
    for i in range(1, n + 1):
        yield i ** 3


n = int(input("Input a number (n):"))

print(f"Cubes from 1 to {n}:")

for cubes in cubes_generator(n):
    print(cubes)


