# Given the list above, write a function that sorts the students in the class based on their id, and returns that list
# Complete the code below so that it returns the list in order of id


def listSort(oldList: list) -> list:
    newList = []
    topNumber = 0 
    for x in oldList:
        idNum = int(x["id"])
        print(idNum)
        if idNum > topNumber:
            topNumber = idNum
            newList.append(x)
        
        elif idNum < topNumber:
            i = 0
            print(len(newList))
            while i < 5:
                print('Index: ', i)
                newIdNum = int(newList[i]["id"])
                if idNum < newIdNum:
                    newList.insert(i, x)
                i += 1
    print(newList)

listSort(digitalcrafts_class)