#Write a program program by using abstractmethod and override the funstions
from abc import ABC, abstractmethod
class Car(ABC):
    def mileage(s):
        pass #placeholder for future code
class Tesla(Car):
    def mileage(s): #overriding function
        print("The mileage is 12kmph")
class Toyota(Car):
    def mileage(s):
        print("The mileage is 13kmph")
class Fortuner(Car):
    def mileage(s): #overriding function
        print("The mileage is 14kmph")
class Sportage(Car):
    def mileage(s):
        print("The mileage is 15kmph")
class Revo(Car):
    def mileage(s):
        print("The mileage is 16kmph")

a=Toyota()
a.mileage()

b=Tesla()
b.mileage()

c=Revo()
c.mileage()

d=Fortuner()
d.mileage()

e=Sportage()
e.mileage()


#Write a program program by using abstractmethod and override the funstions
from abc import ABC,abstractmethod
class Triangle(ABC):
    pass
class First_side(Triangle):
    def side(s):
        return "The First side of Triangle is 15cm"
class Second_side(Triangle):
    def side(s):
        return "The Second side of Triangle is 20cm"
class Third_side(Triangle):
    def side(s):
        return "The Third side of Triangle is 30cm"
print(First_side().side())
print(Second_side().side())
print(Third_side().side())



        

        
