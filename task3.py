#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""

1 = float(input("Enter the first price: "))
2 = float(input("Enter the second price: "))
3 = float(input("Enter the third price: "))
4 = float(input("Enter the fourth price: "))
5 = float(input("Enter the fifth price: "))

import math

subtotal = 1+2+3+4+5
tax = subtotal*0.12
total = subtotal+tax

subtotal = round(subtotal, 2)
tax = round(tax, 2)
total = round(total, 2)

print(f"Your subtotal is ${subtotal} and your taxes total ${tax} for a total of ${total}")
