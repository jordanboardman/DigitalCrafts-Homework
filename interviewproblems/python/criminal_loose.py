# from 8/31/22, NOT COMPLETE
# 2 mile radius
# write a function. which homes should be search? what order?
# Return a list of addresses.

resident_list = [{
    "name": "Bob",
    "distance": 1.2,
    "crimes_committed": 1,
    "address": "4325 Birch St"
},
{
    "name": "May",
    "distance": 0.3,
    "crimes_committed": 3,
    "address": "8903 Trolley St"
},
{
    "name": "Tyler",
    "distance": 0.8,
    "crimes_committed": 0,
    "address": "2348 Magnolia Dr"
},
{
    "name": "Reggie",
    "distance": 0.5,
    "crimes_committed": 1,
    "address": "3478 Seminole Ln"
},
{
    "name": "Seth",
    "distance": 3.2,
    "crimes_committed": 0,
    "address": "9803 Azul St"
},
{
    "name": "Ray",
    "distance": 2.9,
    "crimes_committed": 0,
    "address": "3467 Frost St"
},
{
    "name": "Kim",
    "distance": 0.1,
    "crimes_committed": 0,
    "address": "7893 Daisy Ln"
},
{
    "name": "Lisa",
    "distance": 1.2,
    "crimes_committed": 1,
    "address": "2345 Gale St"
},
{
    "name": "Ashley",
    "distance": 1.5,
    "crimes_committed": 5,
    "address": "6783 Sycamore St"
},
{
    "name": "Turner",
    "distance": 4.3,
    "crimes_committed": 1,
    "address": "8923 Pecan Ln"
},
]

# def forGBI(resident_list) -> list:
    # order = []
    # values = resident_list.values()
    # for x in values:
    #     if x <= 2:
    #         values.sort(order)
    #         values.append(order)
    #         return forGBI
    # print(values)
# index = 0
# while index < len(resident_list):
#     for value in resident_list[index]:
#         print(resident_list[index][value])
#         index += 1

# start of Dre's solution
for perp in resident_list:
    # use bubblesort to arrange address from least distance to greatest.
    for i in range(len(resident_list)):
        for currentIndex in range(0, len(resident_list) - i - 1):
            if perp [currentIndex].get('distance') > perp[currentIndex + 1]:
                perp[currentIndex], perp[currentIndex + 1] = perp[currentIndex + 1], perp[currentIndex]

                print(resident_list)
    # if perp.get('distance') < 2:
        
    #     print(perp)