# # NOT EVEN CLOSE. 
# 
# Create a program that generates 30 students. Each student should have an ID and grade(numerical 0-100).
# # Take those students grades and curve them, the highest grade becoming a 95. Adjust your gradebook to assign a letter grade based on the new values.
# # Write a unittest to verify that your function is working

# # 1. dict of students including name, id, and grade. 
# # 2. Convert numbers and assign letters based on new value.
# # 3. unittest

# students = [{
#     'name': 'cassandra',
#     'ID': 746584736,
#     'grade': 78
# },
# {
#     'name': 'dave',
#     'ID': 758473526,
#     'grade': 69
# },
# {
#     'name': 'wayne',
#     'ID': 839372645,
#     'grade': 90
# },
# {
#     'name': 'garth',
#     'ID': 738473635,
#     'grade': 88
# },
# {
#     'name': 'aang',
#     'ID': 728267354,
#     'grade': 58
# },
# {
#     'name': 'shaggy',
#     'ID': 243546576,
#     'grade': 70
# },
# {
#     'name': 'arnold',
#     'ID': 812374566,
#     'grade': 89
# },
# {
#     'name': 'gerald',
#     'ID': 374859607,
#     'grade': 48
# },
# {
#     'name': 'helga',
#     'ID': 19283746,
#     'grade': 45
# },
# {
#     'name': 'jenny',
#     'ID': 485969708,
#     'grade': 67
# },
# {
#     'name': 'harry',
#     'ID': 102947586,
#     'grade': 93
# },
# {
#     'name': 'ron',
#     'ID': 253647586,
#     'grade': 83
# },
# {
#     'name': 'tim',
#     'ID': 738495867,
#     'grade': 57
# },
# {
#     'name': 'alex',
#     'ID': 102947586,
#     'grade': 68
# },
# {
#     'name': 'daniel',
#     'ID': 362748596,
#     'grade': 67
# },
# {
#     'name': 'manwe',
#     'ID': 384758693,
#     'grade': 91
# },
# {
#     'name': 'frodo',
#     'ID': 920304050,
#     'grade': 69
# },
# {
#     'name': 'sam',
#     'ID': 124356788,
#     'grade': 72
# },
# {
#     'name': 'gandalf',
#     'ID': 405968786,
#     'grade': 92
# },
# {
#     'name': 'bilbo',
#     'ID': 473647586,
#     'grade': 50
# },
# {
#     'name': 'sauron',
#     'ID': 576879808,
#     'grade': 40
# },
# {
#     'name': 'stinky',
#     'ID': 102947586,
#     'grade': 34
# },
# {
#     'name': 'casper',
#     'ID': 273647586,
#     'grade': 82
# },
# {
#     'name': 'fatso',
#     'ID': 475869797,
#     'grade': 46
# },
# {
#     'name': 'cat',
#     'ID': 362734567,
#     'grade': 56
# },
# {
#     'name': 'billy',
#     'ID': 125465768,
#     'grade': 70
# },
# {
#     'name': 'el',
#     'ID': 574857484,
#     'grade': 57
# },
# {
#     'name': 'dustin',
#     'ID': 256728346,
#     'grade': 72
# },
#  {
#     'name': 'mike',
#     'ID': 201928465,
#     'grade': 60
# },
# {
#     'name': 'lucas',
#     'ID': 102946723,
#     'grade': 89
# }]

# def gradeCurve(students):
#     for key in students.items('grade'):
#         print(key)

# gradeCurve(students)

# import random
# import math

# # print(math.floor(random.random() * 1000000000))


# # step 1 create a single with a auto generated id



# # step 2 create 30 students.
# for i in range(1, 30):
#     student = {
#     'id': math.floor(random.random() * 1000000000),
#     'grade': math.floor(random.randint(1, 100))
#     }  

#     # Add each student to the class
#     classroom

#     #  step 3 taking the student with the highest grade and rounding it to a 95.

#         # take the difference between the highest grade and 95, and save the diff
        # ex: 60
        # iterate through the dict and add 60 points to each students grade.

        # step 4 write a switch statement to translate numbers to letter grades.
        # ie 84 -> B 