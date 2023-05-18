#super method is used to call the init method of class which is inherit
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

    @classmethod 
    def change_increment(cls,amount):
        cls.increment=amount         
                                     
    @classmethod                     
    def from_str(cls,emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname,lname,salary)
class Programmer(Employee):
    def __init__(s,fname,lname,salary,proglan,exp):
        super().__init__(fname,lname,salary)
        s.proglan=proglan
        s.exp=exp
    def increase(s):
        s.salary=int(s.salary * (Employee.increment+0.2))

a=Employee("Muhammad","Ali",60000)
a.increase()
print(a.salary)    
b=Programmer("Muhammad","Ali",60000,"Python","5years")
b.increase()
print(b.salary)

