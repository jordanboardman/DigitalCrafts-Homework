# When given two strings for the user, write a function that checks if each string is an anagram of the other. If yes, return true, otherwise false.

#Ex: Debit Card -> Bad Credit
#    Listen -> Silent

from collections import Counter 


s1 = input('Please enter a word: ')
s2 = input('Please enter another word: ')

if (Counter(s1) == Counter(s2)):
        print("Whoa! it's an anagram.")
else:
        print("Bummer! No anagram.")