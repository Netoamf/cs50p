# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:50:01 2023

@author: netoa
"""
import numpy

user_input_X = int(input("Enter a number X: "))
user_input_Y = int(input("Enter a number Y: "))

new_number_power = user_input_X ** user_input_Y
new_number_log = numpy.log2(user_input_X)
print(new_number_power)
print(new_number_log)