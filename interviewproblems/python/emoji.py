# NOT COMPLETE

emojis = ["\U0001F44D", "\N{thumbs up sign}",  "\N{Face with Open Mouth Vomiting}", "\U0001F44D", "\U0001f929", "\N{thumbs down sign}", "\U0001F44E", "\U0001F92E", "\U0001f929", "\N{thumbs down sign}", "\N{thumbs up sign}", "\U0001F44D", "\U0001F44D", "\N{Face with Open Mouth Vomiting}", "\N{thumbs down sign}", "\U0001F44D", "\U0001f929", "\U0001F44D", "\N{thumbs down sign}", "\N{thumbs down sign}"]

# print(emojis)

# emojis needed| thumbs up: "\U0001F44D" +1, starry face: "\U0001f929" +2, thumbs down: "\U0001F44E" -1, vomit face: "\U0001F92E" -2.
# write a function that returns both the percentage of people that liked the movie in general as well as the overall points total.

import random

class Movies:
    def __init__(self):
        self.likeability = 5
    

class Emojis(Movies):

        def thumbsUp(self): 
            damage = +1
            print("\U0001F44D")
        
        def starryFace(self): 
            damage = +2
            print("\U0001f929")
        
        def thumbsDown(self): 
            damage = -1
            print("\U0001F44E")
        
        def vomitFace(self): 
            damage = -2
            print("\U0001F92E")


def chance(self) -> float:
    return random.random() * 100




# Probably thinking too much about this... other people just use for loop with if else as well as using a dict.
