#class method takes object as an argument
class Employee:
    increment=1.5
    no_of_employees=0
    def __init__(s,fname,lname,salary):
        s.fname=fname
        s.lname=lname
        s.salary=salary
        Employee.no_of_employees+=1
    def increase(s):
        s.salary=int(s.salary * Employee.increment)

    @classmethod #decorator
    def change_increment(cls,amount):#ya method hum na isliya banaya ka hum na
        cls.increment=amount         #class ka aik variable ko change karwana tha
                                     #jo class ko as an argument laa raha ha

#This method is used classmethod as a constructor
    @classmethod                     
    def from_str(cls,emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname,lname,salary)
        
a=Employee("Ali","Sheikh",2000)
print(a.salary)
Employee.change_increment(3)
a.increase()
print(a.salary)


##b=Employee.from_str("Mohsin-Sheikh-18100")
##print(b.salary)
