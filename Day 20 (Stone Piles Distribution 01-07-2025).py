# Stone Piles Distribution

'''
We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones.
If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible.
Write a Python program to find the number of stones in each pile.
'''

mylist = []
value = int(input("Enter an integer for the problem: "))

for _ in range(value):
    mylist.append(value)
    value += 2

print(mylist)