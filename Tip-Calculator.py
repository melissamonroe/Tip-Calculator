# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:40:31 2020

@author: Melissa
"""

# tip calculator
# user inputs
# check total
# number of people to split by
# tip percentage

# output total amount of final bill
# total per person
# total tip
# total tip per person


check_amount = float(input("Check amount: $ "))
check_split = 1
check_split = int(input("Split check between how many people? "))
tip_percentage = float(
    input("Tip percent? (15 = 15%) Enter tip percent: ")) / 100

total_check = round(check_amount * (tip_percentage + 1), 2)
total_perperson = total_check / check_split
total_tip = check_amount * tip_percentage
total_tipperperson = total_tip / check_split

print(f'Total check amount is ${total_check}')
print(f'Total per person is ${total_perperson}')
print(f'Total tip amount is ${total_tip}')
print(f'Total tip per person is ${total_tipperperson}')
