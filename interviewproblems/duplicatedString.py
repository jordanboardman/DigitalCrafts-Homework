#Create a list that holds the first name of everyone in this class, return any name that is duplicated


classmates = ['Jordan', 'Jordan', 'Matt', 'An', 'Carlos', 'Wes', 'Fiona', 'Jonathan', 'Jorge', 'Khan']

for i in range(0, len(classmates)):
        for j in range(i+1, len(classmates)):
                if (classmates[i] == classmates[j]):
                        print(classmates[j])

#---------------------------------------------------

#Now, do the same, but using a created function (using def)

