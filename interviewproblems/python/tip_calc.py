# Not quite complete. Still need to adjust decimal numbers to stop after .00 and round up the number? Also do line 11.
# 
# Your task is to write a program that calculates how much of a tip to leave at a restaurant.
# Prompt the user for two things:
# The total bill amount
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:
# good -> 20%
# fair -> 15%
# bad -> 10%
# Allow the ability to divide the check into equal parts amount a number of people. The user will enter the number of people to be divided amongst.

bill_amount = float(input('Total bill amount: '))
level_of_service = input('Good, fair, or bad service? ')

def calcBill():
    if level_of_service == 'Good':
        tip = bill_amount * .20
        print('Tip Amount:','$',tip)
    elif level_of_service == 'fair':
        tip = bill_amount * .15
        print('Tip Amount:','$',tip)
    else:
        tip = bill_amount * .10
        print('Tip Amount:','$',tip)

    total = bill_amount + tip
    print('Total Amount:','$',total)


calcBill()
