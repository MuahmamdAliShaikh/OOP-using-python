##Static function aik asa function hota ha jo na class ko as an argument leta ha or na hi self ko
##it is basically a simple 
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
    @staticmethod
    def isopen(day):
        if day=="Sunday":
            return True
        else:
            return False
#a=Employee("Ali","Sheikh",1000000)
print(Employee.isopen("Tuesday"))

        
