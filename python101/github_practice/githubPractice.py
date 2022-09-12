# *Exercise 1: COMPLETED! 
# Calculate the multiplication and sum of two numbers. Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.*

# Part 1 Values:

# number1 = 20
# number2 = 30
# Expected Output: The result is 600

# Part 2 Values:
    
# number3 = 40
# number4 = 30
# Expected Output: The result is 70

# def num(number1, number2):          # This defines the function, taking in both numbers as parameters.
#     multNum = number1 * number2     # Here the numbers are multiplied. 
#     if multNum <= 1000:             # This statement checks to see if the multiplied number (multNum) is less than or equal to 1000.
#         print(multNum)              # If it is, print the multNum variable.
#     else:                           # If not, print the sum of their numbers (addNum)
#         addNum = number1 + number2
#         print(addNum)

# num(number1, number2)             # In order for the num() function to work, it must be called using ().
                                    # It did not work at first, but then I realized that it needed it's original parameters. Hence the num(number1, number2).
    


# ----------------------------------------------------------------

# DONE (ish)
#*Exercise 2: Print the sum of the current number and the previous number. Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.*

# Expected Output:

# Current Number 1 Previous Number  0  Sum:  1
# Current Number 2 Previous Number  1  Sum:  3
# Current Number 3 Previous Number  2  Sum:  5
# Current Number 4 Previous Number  3  Sum:  7
# Current Number 5 Previous Number  4  Sum:  9
# Current Number 6 Previous Number  5  Sum:  11
# Current Number 7 Previous Number  6  Sum:  13
# Current Number 8 Previous Number  7  Sum:  15
# Current Number 9 Previous Number  8  Sum:  17




# previous_num = 0

# for current_num in range(0, 11):
    
#     addedNum =  current_num + previous_num
#     sumNum =  previous_num + addedNum
#     print('Current number: ', current_num, 'Previous number: ', addedNum, 'Sum: ', sumNum)

# This is Dez's solution which was similar to mine, but my output was slightly off.
# previous_num = 0                            # Set up the initial value of the previous number globally. 

# for current_num in range(1, 11):            # Set up your for loop from 1 to 10
#     sum_value = previous_num + current_num  # Assign the previous number plus the current number to the variable sum_value
#     print("Current Number:", current_num, "Previous Number:", previous_num, " Sum:", sum_value) 
# #     # Modify the previous number variable by setting it to the current number variable each time it iterates through the loop
#     previous_num = current_num


# ----------------------------------------------------------------


#*Exercise 3 PART 1: Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Concatenate strings to print the resulting output message. *

# Expected Output:

# Dezarea will be 100 years old in 2095.





#*Exercise 3 PART 2: Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old, except use f-strings instead of the + operator to print the resulting output message. *

# Expected Output:

# Dezarea will be 100 years old in 2095.






# *Exercise 4: Ask the user for a number. Depending on whether the number is even or odd, print out an even or odd message to the user. *

# Expected Output (if even number):

# Even Number



# Expected Output (if odd number):

# Odd Number





# *Exercise 5: Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function. *

# Expected Output

# [5, 25]





# *Exercise 6: Print characters from a string that are present at an even index number. Write a program to accept a string from the user and display characters that are present at an even index number. *


# Expected Output if the original string was dezarea:
# d
# z
# r
# a



# *Exercise 7: Write a program to remove characters from a string starting from zero up to x and return a new string. 

# For example:

# remove_chars("dezbryan", 4) so output must be ryan. Here we need to remove first four characters from a string.
# remove_chars("dezbryan", 2) so output must be zbryan. Here we need to remove first two characters from a string.
# Note: x must be less than the length of the string.



# * Exercise 8: Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.*

# For example:

# x: [10, 20, 30, 40, 10]
# True

# y = [75, 65, 35, 75, 30]
# False



#  * Exercise 9: Iterate the given list of numbers and return to a new list only those numbers which are divisible by 5 *

# For example: 

# list =  [10, 20, 33, 46, 55]
# Divisible by 5, output will be
# [10, 20, 55]



#  * Exercise 10: Write a program to find how many times substring “Dez” appears in the given string. *

# x = "Dez is good developer. Dez is a turkey."

# Expected Output:

# 2



#  * Exercise 11: Print the following pattern *

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 



#  * Exercise 12: Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list. *

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# Expected Output:

# [25, 35, 40, 60, 90]



#  * Exercise 13: Write a Program to extract each digit from an integer in the reverse order. *

# For example: 
    
# If the given int is 7536, the output is “6357“.



#  * Exercise 14: Print multiplication table from 1 to 10. *

# Expected Output:

# 1  2 3 4 5 6 7 8 9 10 		
# 2  4 6 8 10 12 14 16 18 20 		
# 3  6 9 12 15 18 21 24 27 30 		
# 4  8 12 16 20 24 28 32 36 40 		
# 5  10 15 20 25 30 35 40 45 50 		
# 6  12 18 24 30 36 42 48 54 60 		
# 7  14 21 28 35 42 49 56 63 70 		
# 8  16 24 32 40 48 56 64 72 80 		
# 9  18 27 36 45 54 63 72 81 90 		
# 10 20 30 40 50 60 70 80 90 100 



#  * Exercise 15: Print downward Half-Pyramid Pattern with Star (asterisk) *

# Expected Output:

# * * * * *  
# * * * *  
# * * *  
# * *  
# *



#  * Exercise 16: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exponent. *

# Expected output

# Example 1:

# base = 2
# exponent = 5

# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

# Example 2:

# base = 5
# exponent = 4

# 5 raises to the power of 4 is: 625 
# i.e. (5 *5 * 5 *5 = 625)



#  * Exercise 17: Using file handling, write a function in Python to count and display the total number of words in a text file. *

# Expected output if your document had 7 words:

# Total words are: 7



#  * Exercise 18: Using file handling, write a function in Python to read lines from a text file. Your function should find and display the occurrence of the word "the", both upper and lower case! *

# For example: If the content of the file is:

# "We will be learning about bootstrap today! This file will also be the file that is used for our additional practices. The individuals that do the extra practice are certainly going to benefit from putting in the extra work."

# The output should be 4. 




#  * Exercise 19: Using file handling, write a function to read lines from a text file and display those words which are less than 4 characters. *

# For example: If the content of the file is:

# "We will be learning about bootstrap today! This file will also be the file that is used for our additional practices. The individuals that do the extra practice are certainly going to benefit from putting in the extra work."

# The expected output should be: We be be the is for our The do the are to in the 




#  * Exercise 20: Using file handling, write a function to count the words "this" and "that" present in a text file. *

# For example: If the content of the file is:

# "We will be learning about bootstrap today! This file will also be the file that is used for our additional practices. The individuals that do the extra practice are certainly going to benefit from putting in the extra work."

# The expected output should be: 8




#  * Exercise 21: Using file handling, write a function to count words in a text file those are ending with letter "e". *

# For example: If the content of the file is:

# "We will be learning about bootstrap today! This file will also be the file that is used for our additional practices. The individuals that do the extra practice are certainly going to benefit from putting in the extra work."

# The expected output should be: 11




#  * Exercise 22: Using file handling, write a function to count uppercase character in a text file. *

# For example: If the content of the file is:

# "We will be learning about bootstrap today! This file will also be the file that is used for our additional practices. The individuals that do the extra practice are certainly going to benefit from putting in the extra work."

# The expected output should be: 3




#  * Exercise 23: The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in. *

# For example:

# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True




#  * Exercise 24: Imagine that we have two monkeys, and the parameters a_smile and b_smile indicate if each monkey is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble and False if we are in the clear. *

# For example:

# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False