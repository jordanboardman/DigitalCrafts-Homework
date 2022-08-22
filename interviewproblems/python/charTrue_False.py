# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if: Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order. Example 1: Input: s = "()" Output: true Example 2: Input: s = "()[]{}" Output: true Example 3: Input: s = "(]" Output: false

userInput = input('Type in a combination of open/close characters, i.e.: ( ), { }, and/or [ ]: ' )

# Things to check: 
#   If string is odd or even. If odd, output = false
#   If string enters a parenthesis, curly brace, or bracket, check for corresponding closing parenthesis, curly brace, or bracket

# Need two pointers, one at beginning and one at end

# Make sure user only inputs what the prompt is asking for. ex | 'Please enter a valid input'




# def openClose(stringInput: str) -> bool:
#     if len(stringInput) % 2 == 1:
#         return False
#     else:
#         openCloseDict = {'(': 0,
#                          ')': 0,
#                          '[': 0,
#                          ']': 0,
#                          '{': 0,
#                          '}': 0}


#         return True



# print(openClose(userInput))

open_list = ["[","{","("]
close_list = ["]","}",")"]
  
# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

print(check(userInput))
  
# Driver code
# string = "{[]{()}}"
# print(string,"-", check(string))
  
# string = "[{}{})(]"
# print(string,"-", check(string))
  
# string = "((()"
# print(string,"-",check(string))