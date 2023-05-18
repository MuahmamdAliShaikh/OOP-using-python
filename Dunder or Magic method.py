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
    def __add__(s,other):
        s.salary=s.salary+other.salary
        return s.salary
    def __repr__(s):
        return "Employee({},{},{})".format(s.fname,s.lname,s.salary)
    def __str__(s):
        return "The name of employee is {}".format(s.fname + s.lname)
    

Ali=Programmer("Ali","Shaikh",50000,"PHP","5 years")
Mohsin=Programmer("Mohsin","Shaikh",50000,"PHP","5 years")
#print(Ali+Mohsin)

print(Ali)
print(repr(Ali))
#print(str(Mohsin))



#a=5
#print(a.__mul__(15))

