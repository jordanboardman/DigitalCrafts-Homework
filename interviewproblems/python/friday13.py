# Write a function in python to detect if it's Friday the 13th. The function can accept two parameters. The first parameter will be the number indicating the month, and the second will be the year in four digits. Return True when the month contains a Friday the 13th, else return False.

# 1. Google if i can import python calendar. Done
# 2. Create variables. Done
# 3. Start function where it takes in the two variables. Done
# 4. I'm guessing a loop that looks for friday=true and 13=true.
# 5. If else statement checking for number 4 otherwise false.

import calendar


year = 2022
month = 5

def yesMonth(year, month):
    
    for i in range(1, calendar.monthlen(year, month) + 1):
        # yield date(year, month, i)

    # for d in date_iter(year, month):
        print(d)

# Maybe this?
# for d in [x for x in c.itermonthdates(2019, 7) if x.month == 7]:


    print(calendar.month(year, month))

