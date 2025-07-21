# Write a Python program to find the XOR of two given strings interpreted as binary numbers.

mylist = ['100011101100001', '100101100101110']

a = int(mylist[0],2)
b = int(mylist[1],2)

xor = a ^ b

print(bin(xor))