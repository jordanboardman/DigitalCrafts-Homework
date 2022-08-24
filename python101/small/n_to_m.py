# 8. n to m
# Same as the previous problem (loop_1_to_10.py), except you will prompt the user for the number to start on and the number to end on. Example session:

# $ python3 n_to_m.py
# Start from: 2
# End on: 8
# 2
# 3
# 4
# 5
# 6
# 7
# 8

startNum = int(input('Start Number: '))
endNum = int(input('End Number: '))

i = startNum
j = endNum

while i <= j:
    print(i)
    i += 1

# I figured this out in under 10 minutes using loop_to_10.py as a reference!