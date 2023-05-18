class Vehicle:
    def __init__(self,name,price,model):
        self.name=name
        self.price=price
        self.model=model
    def show_details(self):
        return f"The Name of Vehicle: {self.name} \nThe Price of Vehicle: {self.price}\nThe Model of Vehicle: {self.model}"
    def speed(self):
        return f"The Speed of Vehicle is 360kmph"
class Car(Vehicle):
    def show_details(self):
        return f"The Name of Car: {self.name} \nThe Price of Car: {self.price}\nThe Model of Car: {self.model}"
    def speed(self):
        return f"The Speed of Car is 260kmph"
class Truck(Vehicle):
    def show_details(self):
        return f"The Name of Truck: {self.name} \nThe Price of Truck: {self.price}\nThe Model of Truck: {self.model}"
    def speed(self):
        return f"The Speed of Truck is 4000kmph"

a=Vehicle("Honda",2566155,2022)
print(a.show_details())
print(a.speed())
a=Car("Revo Rocco",2566155,2012)
print(a.show_details())
print(a.speed())
a=Truck("Tanker",2566155,2016)
print(a.show_details())
print(a.speed())