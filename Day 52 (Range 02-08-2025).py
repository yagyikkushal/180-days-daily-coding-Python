# Write a Python program to find the largest integer divisor of a number n that is less than n.

n = 6500
temp = 0

for _ in range(n - 1, 0, -1):
    if n % _ == 0:
        temp = _
        break

print(_)