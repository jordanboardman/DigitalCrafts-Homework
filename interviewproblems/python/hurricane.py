#only tropical TS & above receive a name.
#TD just get numbers
#Generate 25 storms per simulation.


import random

class Hurricane:
    def __init__(self, name: str, cat: str, destination: str, travelspeed: int):
        self.name = name
        self.cat = cat
        self.destination = destination
        self.travelspeed = travelspeed
        

terry = Hurricane("Terry", "Cat5", "Charleston", 70)

tsHuey = Hurricane('Huey', 'TS', 'Charleston', 50)

td1 = Hurricane('none', 'TD', 'Charleston', 10)

s4 = Hurricane('none', 'Cat4', 'Charleston', 10)
s3 = Hurricane('none', 'Cat3', 'Charleston', 10)
s2 = Hurricane('none', 'Cat2', 'Charleston', 10)
s1 = Hurricane('none', 'Cat1', 'Charleston', 10)

    # def chance(self) -> float:
    #     return random.random() * 100


