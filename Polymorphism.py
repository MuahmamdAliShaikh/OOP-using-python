#Polymorphism means different forms and in which the same name function is used for different data types.
#Function overloading:The process where the same function can be used multiple times by passing a
#different number of parameters as arguments.
#Method overriding:when you have two methods with the same name that each perform different tasks.
'''class PAK():
    def capital(s):
        print("The Capital of Pakistan is Islamabad")
    def language(s):
        print("The National language of Pakistan is Urdu")
    def type(s):
        print("The Pakistan is developing country")
class USA():
    def capital(s):
        print("The Capital of USA is Washington DC")
    def language(s):
        print("The National language USA is English")
    def type(s):
        print("The USA is developed country")
obj1=PAK()
obj2=USA()
for country in (obj1,obj2):
    country.capital()
    country.language()
    country.type()'''

'''class PAK():
    def capital(s):
        print("The Capital of Pakistan is Islamabad")
    def language(s):
        print("The National language of Pakistan is Urdu")
    def type(s):
        print("The Pakistan is developing country")
class USA():
    def capital(s):
        print("The Capital of USA is Washington DC")
    def language(s):
        print("The National language USA is English")
    def type(s):
        print("The USA is developed country")
def func(obj):
    obj.capital()
    obj.language()
    obj.type()
func(PAK())
func(USA())'''

class Bird:
    def intro(s):
        print("There are different types of birds")
    def flight(s):
        print("Most of the birds can fly but some cannot")
class Sparrows(Bird):
    def flight(s):
        print("Sparrow can fly")
class Ostriches(Bird):
    def flight(s):
        print("Ostrich cannot fly")
obj1=Bird()
obj2=Sparrows()
obj3=Ostriches()

obj1.intro()
obj1.flight()

obj2.intro()
obj2.flight()

obj3.intro()
obj3.flight()



        



    

    
