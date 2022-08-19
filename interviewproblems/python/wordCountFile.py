# WRITE A FUNCTION that reads a file. Return and print the word in the file appears the most

# Iterate through the file and return the words that appears the most. i.e if the word 'the' appears 16 times, keep track of it are return it to the function caller as well as print it to the screen

# no need to create new txt file and copy and paste. can use copy path or copy relative path.
file = open('justToSay.txt', 'w')


file.write('I have eaten the plums that were in the icebox and which you were probably saving for breakfast Forgive me they were delicious so sweet and so cold\n')
file.close()


# also just use open(), not need to use file.
file = open('justToSay.txt', 'r')
print(file.read())
file.close()

for count, value in enumerate(file):
        print(count, value)

# for word in range(len(file)):
#     file = file[word]
#     print(word, file)

# f = file("justToSay.txt").read()
# for word in f.split():
#     # do something with word
#     print(file.read())

# file.close()




