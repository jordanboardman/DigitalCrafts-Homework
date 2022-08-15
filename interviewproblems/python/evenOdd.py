#(NOT COMPLETE, FUNCTION IS NOT WRITTEN)
# 
#Given a list of numbers, write a function that tallies the number even and odd occurences and return the results. 
# Ex. [3, 564, 44, 65, 52, 2, 7] -> (Odd: 3, Even: 4)
#Write a unit test to prove your function works.

#Create a list
myList = [45, 33, 567, 3322, 456, 1075, 478]

#Create a function for even and odd tally
# def tallyEvenandOdd(myList) :
even_count, odd_count = 0, 0

#Iterate through list to find results.
for num in myList:
        if num % 2 == 0:
            even_count += 1

        else: 
            odd_count += 1

#Print results.
print("Odd :", odd_count, "Even: ", even_count)
