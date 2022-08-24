# Medium #4 | not completed

try:
    widthinput = int(input('Type in your desired width: '))

except: 
    print('Please enter a positive number')

if widthinput > 0:
    try: 
        heightinput = int(input('Type in your desired height '))

    except:
        print('Please enter a positive integer')

else:
    print('Invalid input')

if heightinput > 0:
    
    toprow = ''
    dot = '*'
    count1 = 0

    while widthinput > count1:
        toprow = toprow + dot
        count1 = count1 + 1
    print(toprow)

    midrow = ''
    count2 = 0
    while count2 < heightinput -2:
        count3 = 0
        midrow = midrow + dot
        while count3 < widthinput -2:
            midrow = midrow + ' '
            count3 = count3 + 1
            midrow = midrow + dot
        print(midrow)
        count2 = count2 + 1
    
else: 
    print('Invalid Input')

print(toprow)

