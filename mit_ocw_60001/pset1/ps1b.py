# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 17:13:20 2023

@author: netoa
"""

total_cost = float(input("What is the total cost of your dream house? "))
annual_salary = float(input("insert annual salary: "))
portion_saved = float(input("how much do you save each month, as a decimal? "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal:"))
current_savings = 0
portion_down_payment = total_cost * .25
monthly_salary = annual_salary / 12
months = 0

r = .04


while current_savings <= portion_down_payment:
   current_savings += (monthly_salary * portion_saved) + (current_savings * r)/12
   months = months + 1
   
   if months % 6 == 0 and months > 0:
       monthly_salary += monthly_salary*semi_annual_raise
       print("new monthly salary: ", monthly_salary)


print('Number of months: ', months)