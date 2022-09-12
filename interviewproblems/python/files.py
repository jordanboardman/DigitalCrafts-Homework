# # Using files.txt and files_2.txt
# Given a file, write a function that swap all cases. All uppercase letters should become lower case and vice versa. Write unit tests to confirm 

# Overwrite to new variable next.


import unittest

def changeCaps():

    file = open('files.txt', 'r')
    for x in file:
        print(x.swapcase())


    file.close()

    
changeCaps()

def changeCaps_2():

    file_2 = open('files_2.txt', 'r')
    for x in file_2:
        print(x.swapcase())


    file_2.close()

changeCaps_2()

# unittest
class TestCaps(unittest.TestCase):

    # After making overwrite portion of the code, call both using .read() in the self parameters.

    
    def test_changeCaps(self):
        self.assertEqual(changeCaps())


    
    def test_changeCaps_2(self):
        self.assertEqual(changeCaps_2())


unittest.main()