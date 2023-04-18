# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:02:31 2023

@author: netoa
"""
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

largest_odd = None

if x % 2 == 1:
    largest_odd = x

if y % 2 == 1:
    if largest_odd is None or y > largest_odd:
        largest_odd = y

if z % 2 == 1:
    if largest_odd is None or z > largest_odd:
        largest_odd = z

if largest_odd is not None:
    print("The largest odd number is:", largest_odd)
else:
    print("None of the numbers are odd.")




