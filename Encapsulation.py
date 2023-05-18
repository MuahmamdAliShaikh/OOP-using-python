##public - members are accessible from outside the class. private - members cannot be accessed (or viewed)
##from outside the class. protected - members cannot be accessed from outside the class, however, they can
##be accessed in inherited classes.
##Encasulation:Describe the concept of bundling data and methods with in a single unit
##A class is an examples of encapsulation as it finds all the data
##members (instance variable ) and methods
##Create an employeee class by defining employee attributes such as name and salary as an instance variable and using work() and show() instance methods
##class Employee:
##    def __init__(s,name,salary,project):
##        s.name=name
##        s.salary=salary
##        s.project=project
##    def work(s):
##        print(s.name,"is working on",s.project)
##    def show(s):
##        print("Name:",s.name,"\nProject:",s.project)
##    def net_salary(s):
##        print("The net income of",s.name,"is",s.salary*12)
##emp=Employee("Ali",500000,"NLP")
##emp.show()
##emp.work()
##emp.net_salary()


##Access Protected member within the class and its sub_class using instance method
##Protected members are accessible within the class and also available to its sub-classes
##class Company:
##    def __init__(s,name,salary):
##        s.name=name
##        s._salary=salary
##    
##class Employee(Company):
##    def __init__(s,project):
##        s.project=project
##        Company.__init__(s,"Ali",50000)
##    def show(s):
##        print("Name:",s.name,"\nProject:",s.project,"\nSalary:",s._salary)
##
##emp=Employee("NLP")
##emp.show()

##Private members are accessible only within the class, and we can’t access them directly from the class objects.    
class Employee:
    def __init__(s,salary,name):
        s.__salary=salary
        s.name=name
        
    def show(s):
        print(s.name,"is earning",s.__salary,"millions dollars from UNO")

emp=Employee(2,"Ali Shaikh")
emp.show()



