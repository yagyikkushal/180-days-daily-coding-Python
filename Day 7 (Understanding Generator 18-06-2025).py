# Write a Python program that uses a generator to produce cubes from 1 to n, then sums these cubes and prints the result.


def cube_gen(c):
    yield c ** 3


def cube_sum(n):
    sum_gen = 0
    for i in range(1, n + 1):
        sum_gen = sum_gen + next(cube_gen(i))

    print(sum_gen)


cube_sum(3)