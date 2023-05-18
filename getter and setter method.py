'''class Student:
    def __init__(s,name,age):
        s.__age=age
        s.name=name
    def get_age(s):
        return s.__age
    def set_age(s,age):
        s.__age=age

stud=Student("Ali",20)
print("Name:",stud.name,"Age:",stud.get_age())
stud.set_age(16)
print("Name:",stud.name,"Age:",stud.get_age())'''

class Student:
    def __init__(s,name,age,roll_no):
        s._age=age
        s.name=name
        s.__roll_no=roll_no
    
    def get_rollno(s):
        return s.__roll_no
    def set_rollno(s,roll_no):
        if roll_no>50:
            print("Invalid roll number.Please set correct roll number ")
        else:
            s.__roll_no=roll_no
            
stud=Student("Ali",20,25)
print("Name:",stud.name,"Age:",stud._age,"Roll no:",stud.get_rollno())
stud.set_rollno(85)
print("Correct roll no",stud.get_rollno())


