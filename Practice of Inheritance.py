#The class from which we inherit called the Parent Class, Superclass, or Base Class.
#The new class which was created by inheriting functionalities of the parent class
#is called Child Class, Derived Class, or Subclass.
class Vehicle:
    def __init__(s,seat_cap):
        s.seat_cap=seat_cap
        s.fare_char=int(s.seat_cap * 200)
        
class Bus(Vehicle):
    def __init__(s,seat_cap):
        Vehicle.__init__(s,seat_cap)
    def final_amount(s):
        total_fare=int(s.fare_char+(0.2*s.fare_char))
        return total_fare

a=Bus(100)
print(a.final_amount())
'''class Vehicle:
    def __init__(s,seat_cap):
        s.seat_cap=seat_cap
        s.fare_charges=int(s.seat_cap*100)
class Bus(Vehicle):
    def __init__(s,seat_cap):
        super().__init__(seat_cap)
    def total_fare(s):
        final_amount=int(s.fare_charges + (0.1*s.fare_charges))
        return final_amount

a=Bus(50)
print(a.total_fare())'''

    


    
