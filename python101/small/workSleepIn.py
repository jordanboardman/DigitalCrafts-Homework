# # 5. Work or Sleep In?
# Prompt the user for a day of the week just like the previous problem. But this time, print "Go to work" if it's a work day and "Sleep in" if it's a weekend day. Example session:

# $ python3 work_or_sleep_in.py
# Day (0-6)? 5
# Go to work
# $ python work_or_sleep_in.py
# Day (0-6)? 6
# Sleep in

day = int(input('Day (0-6)? '))

if (day == 0) or (day == 6):
    print('sleep in')
elif day <= 5:
    print('go to work')
else:
    print('type a number 0-6')

# I solved this one once I figured out that you can use or (like in line 13) as long as both conditions are in (). I also had to think a little less. No array was needed for this, it's really just a math problem with a string answer, not integer.