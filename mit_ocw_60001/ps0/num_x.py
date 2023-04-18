# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:57:05 2023

@author: netoa
"""

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
count = 0

while count < numXs:
    toPrint += 'X'
    count += 1

print(toPrint)