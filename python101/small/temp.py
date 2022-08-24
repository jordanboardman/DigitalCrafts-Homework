# 6. Celsius to Fahrenheit
# Prompt the user for a number in degrees Celsius, and convert the value to degrees in Fahrenheit and display it to the user.

# Use the following formula:

# F = (C * 9/5) + 32
# Example sessions:

# $ python3 degree_conversion.py
# Temperature in C? 28
# 82.4 F
# $ python3 degree_conversion.py
# Temperature in C? -5
# 23 F

celsTemp = int(input("What's the temp in C?"))

F = (celsTemp * 9/5) + 32

print(F)

# I figured this one out without Google and on my first try!!