# Write a Python function that print cubes of numbers from 1 to n.


def cube_gen(n):
    for i in range(1, n + 1):
        print(i ** 3)


cube_gen(6)