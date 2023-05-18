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

ali=Employee("Ali","Sheikh",50000)
ali.increment=9 #it is add new variable into a list
print(ali.__dict__)#it show all instance variables into a list
print(ali.salary)
ali.increase()
print(Employee.__dict__)#it show all class variables into a list
print(ali.salary)
print(ali.no_of_employees)


zain=Employee("Zain","Mughal",20000)
print(zain.no_of_employees)
