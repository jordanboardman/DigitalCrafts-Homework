# #4. Day of the Week (NOT COMPLETED)
# Given the following code which prompts the user for a day number (Remember that the int function converts a numeric string to a number):

# day = int(input('Day (0-6)? '))
# # Fill in your code here
# The user will enter a number from 0 to 6. Given this number, print a day of the week. 0 for Sunday, 1 for Monday, 2 for Tuesday, and so on. Here's an example user session (this assumes you've named the file day_of_week.py):
# $ python3 day_of_week.py
# Day (0-6)? 5
# Friday
# $ python day_of_week.py
# Day (0-6)? 0
# Sunday
#---------------------------------------------

# 1. Use given day variable.
# 2. Make a list of days?
# 3. print day with index of ? 

from operator import indexOf


day = int(input('Day (0-6)? '))

daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

print(indexOf(day))