# Write a Python program that accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34.

value_to_check = int(input(
    "Enter an integer to check whether it is greater than 4^4 and whether it leaves remainder as 4 when divided by 34: "))

if value_to_check > 256 and value_to_check % 34 == 4:
    print("True")
else:
    print("False")

# Remember the symbol of modulo operator and it gives remainder in divide.