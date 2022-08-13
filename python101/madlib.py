# 3. Madlib
# Prompt the user for the missing words to a Madlib sentence using the input function. You can make up your own Madlib sentence, but here's an example:

# ____(name)____'s favorite subject in school is ____(subject)____.
# With the above given sentence, this is what a user session might look like:

# $ python3 madlib.py
# Please fill in the blanks below:
# ____(name)____'s favorite subject in school is ____(subject)____.
# What is name? Marty
# What is subject? time travel
# Marty's favorite subject in school is time travel.
#------------------------------------------------------
# 1. create variables for name and subject with input(). 
# 2. create inputs with variables placed inside.
# 3. print result.

intro = input('Madlib time!')

name = input('Please enter a name: ')
subject = input('Please enter a school subject: ')

print("%s's favorite subject in school is %s." % (name.capitalize(), subject))