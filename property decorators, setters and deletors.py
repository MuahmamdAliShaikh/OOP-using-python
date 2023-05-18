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

    @property #By the help of this operator we call email function as a attribute
    def email(s):
        if s.fname==None:
            return "Email not set"
        else:
            return s.fname +'.'+ s.lname + '@gmail.com'

    @email.setter #we used this setter bcz when we want to change email attribute it will through error
    #we used this for settlement of new email as an attribute
    def email(s,given_email):
        name_list=given_email.split('@')[0].split('.') #first we split email from @ then
    #we have fname.lname and then split it from . two names fname on 0 index and lname on 1 index
        s.fname=name_list[0]
        s.lname=name_list[1]

    @email.deleter
    def email(s):
        s.fname=None
        s.lname=None

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


'''if wali condition iss liya used hoti ha ka hum jab bhi agar file ko import karein to iss file ka functions
wahan print na hon'''
#if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported
if __name__=='__main__':
    Ali=Employee("Ali","Shaikh",50000)
    print(Ali.email)
##    Ali.lname="Khan"
    Ali.email="Sheikh.Ali@gmail.com" 
    print(Ali.email)
    del Ali.email
    print(Ali.email)

