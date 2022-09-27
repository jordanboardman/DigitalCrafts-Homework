# Mastermind (Coded along with Dre. Not done, check web-ft-08-22)
# A low-level implementation of the classic game “Mastermind”. We need to write a program that generates a four-digit random code and the user needs to guess the code in 10 tries or less. If any digit out of the guessed four-digit code is wrong, the computer should print out “B”. If the digit is correct but at the wrong place, the computer should print “Y”. If both the digit and position is correct, the computer should print “R”.

# Correct Digit: 5348 -> User Guess: 5182 -> RBYB

# Write a function that starts the game, it should either win or loss depending on the result, write a unit test to verify that your game works

# 1. generate random number (or type for now).
# 2. write user input sequence. user gets 10 tries to guess number.
# 3. wrong number = B, correct (wrong spot) = Y, correct number and position = R. 


import random

# Random number generator

def mastermind():
    # Generate each number individually then concat them.

    answer = generateNumber()
    turns = 0
    win = False

    print('Welcome to Mastermind!')
    while turns <= 10 and win == True:
        guess = input('Enter a number: ')
        if checkGuess(guess, answer) == True:
            win = True
            print("You've Won!")
        turns += 1
    
    if turns >= 10:
        print("You've Lost!")

    # print('Answer: ', answer)
    # print('Guess: ', guess)

def generateNumber() -> str:
    number = ''
    for num in range(0,4):
        number += str(random.randint(0,9))

    return number

def checkGuess(guess: str, answer: str) -> bool:
    hint = ''
    for i in range(0,4):
        if guess[i] == answer[i]:
            hint += 'R'
        elif guess[i] in answer:
            hint += 'Y'
        else:
            hint += 'B'

        return hint == 'RRRR'

mastermind()







# def userStuff():
#     num = 5784
#     nums = []
#     list_length = 10

#     for i in range(list_length):
#         userNum = userInput = int(input("enter 4 numbers. you have 10 tries to guess the right sequence of numbers: "))
#         nums.append(userNum)    
    
#     print(nums)

# userStuff()

# print(userInput)

# def Mastermind(num, userInput):
#     i = 1
#     while i in userInput <= 10:
#         print (i)
#         i += 1

# Mastermind(num, userInput)