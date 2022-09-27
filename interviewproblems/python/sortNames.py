# Given an array, write a function that sorts all names in reverse from Z-A. Write a unit test using the names of every student in this class to verify your solution.

# USE BUBBLE SORT AND BUILD THE FUNCTION FROM SCRATCH. DON'T USE BUILT IN FUNCTIONS, BECAUSE (APPARENTLY), INTERVIEWERS WILL THINK YOU DON'T KNOW WHAT YOU'RE DOING IF YOU USE A BUILT IN FUNCTION.

def sortNames():
    names = ['aria', 'jon', 'ned', 'tyrion', 'jamie', 'breann']

    names.sort(reverse= True)

# def sortNames(names):
#     revNames = names.sort(reverse = True)

    print(names)

sortNames()

# unittest

