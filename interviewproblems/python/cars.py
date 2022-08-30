# create a class called car.
# 2 child classes, 1 for electric, 1 for gas.
# all cars get= curb weight, top speed, all wheel/rear wheel, horsepower.
# all cars can acceleerate, brake and reverse.   
#     when accelerate, print moving, braking print stopping, reversing print backing up.
# electric get battery capacity and range.
# evs get a function called charging that prints charging.
# ICE vehicles get mpg and a function to refill.


# parent class
class Car:
   def __init__(self, curbweight: int, topspeed: int, wheel: str, horsepower: int):
    self.curbweight = curbweight
    self.topspeed = topspeed
    self.wheel = wheel
    self.horsepower = horsepower

    def accelerate(self):
        print('moving')
    
    def brake(self):
        print('stopping')
    
    def reverse(self):
        print('backing up')

# child classes
class Electric(Car):
    def __init__(self, curbweight: 3700, topspeed: 170, wheel: str, horsepower: 60, battery: int, carRange: int, ):
       super().__init__(curbweight, topspeed, wheel, horsepower)
       self.battery = battery
       self.carRange = carRange

    def charging(self):
        print('charging')

class Gas(Car):
    def __init__(self, curbweight: 4200, topspeed: int, wheel: str, horsepower: int, mpg: int):
       super().__init__(curbweight, topspeed, wheel, horsepower)
       self.mpg = mpg
        
    def refill(self):
            print('refilling')

# Next would be to create callers for all of this code.
# such as, is someone entered Tesla, what parameters would it show and what functions would it use?