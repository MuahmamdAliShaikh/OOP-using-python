import re
class Employee:
    def __init__(self):
        self.data=[]
        self.salary=""
    def emp_types(self):
        print("""
              1.Hourly
              2.Daily
              3.Yearly""")
        user=int(input("ENTER CHOICE NO: "))
        if user==1:
            self.salary="hourly"
        elif user==2:
            self.salary="daily"
        elif user==3:
            self.salary="yearly"
        else:
            print("INVALID OPTION")
    def find_data(self):
        f=open("Emp.txt","r")
        c=f.readlines()
        for i in c:
            x=re.split(",|\n",i)
            self.data.append(x)
    def show_data(self):
        k=0
        for i in range(len(self.data)):
            if self.data[i][3]==self.salary:
                print("EMPLOYEE NAME: ",self.data[i][0].upper(),"EMPLOYEE AGE: ",self.data[i][1],"EMPLOYEE DESIGNATION: ",self.data[i][2].upper(),"EMPLOYEE SALARY: ",self.data[i][4],'$')
            else:
                k+=1
        if k==len(self.data):
            print("NO RECORD FOUND")
        self.emp_types()
        self.show_data()

        
               
a=Employee()
a.emp_types()
a.find_data()
a.show_data()





    
    
