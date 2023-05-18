##Bank system
##Essential name,pin
##controler Create Account,Cash Deposit,cash withdrawal,Show balance
##class Bank:
##    def __init__(s):
##        s.pin=""
##        s.balance=0
##        s.name=""
##        s.show_function()
##    def show_function(s):
##        print('''
##               1.CREATE ACCOUNT
##               2.CASH DEPOSIT
##               3.CASH WITHDRRAWL
##               4.SHOW BALANCE''')
##        choice=int(input("Enter the choice"))
##        if choice==1:
##            s.create_acc()
##            s.show_function()
##        elif choice==2:
##            s.cash_dep()
##            s.show_function()
##        elif choice==3:
##            s.cash_with()
##            s.show_function()
##        elif choice==4:
##            s.show_balance()
##            s.show_function()
##        else:
##            print("Enter your choice")
##            
##    def create_acc(s):
##        s.name=str(input("Enter your full name"))
##        s.pin+=str(input("Create your Pin"))
##        print("Account Created SuccessfullY")
##    def cash_dep(s):
##        user=str(input("Enter Your Name: "))
##        pinc=str(input("Enter your Pin: "))
##        if user==s.name and pinc==s.pin:
##            s.balance+=int(input("Enter the amount for Deposit:"))
##            print("Deposited Successfully")
##        else:
##            print("Invalid Password")
##            
##    def cash_with(s):
##       user=str(input("Enter your Name: "))
##       pinc=str(input("Enter your Pin: "))
##       if user==s.name and pinc==s.pin:
##           amount=int(input("Enter Amount for withdrawal: "))
##           if amount<=s.balance:
##               s.balance-=amount
##           else:
##               print("Insufficient balance")
##       else:
##          print("Invalid Username or Pin")
##    def show_balance(s):
##        user=str(input("Enter Your Name: "))
##        pinc=str(input("ENter your Pin: "))
##        if user==s.name and pinc==s.pin:
##           print("The available credit is ",s.balance)
##a=Bank()
##a.show_function()
##a.create_acc()
##a.cash_dep()
##a.cash_with()
##a.show_balance()
      


class BankSys:
    def __init__(s):
        s.name=""
        s.pin=0
        s.balance=0
        #s.show_func()
    def show_func(s):
        print("""
                 1.Create Account
                 2.Cash Deposit
                 3.Cash Withdrawal
                 4.Balance""")
        choice=int(input("Enter Option: "))
        if choice==1:
            s.Create_acc()
            s.show_func()
        elif choice==2:
            s.Cash_dep()
            s.show_func()
        elif choice==3:
            s.Cash_with()
            s.show_func()
        elif choice==4:
            s.Balance()
            s.show_func()
        else:
            choice=int(input("Enter Given Option: "))
        
    def Create_acc(s):
        s.name=input("Enter Name: ")
        s.pin=int(input("Enter Pin: " ))
        print("Created Account Successfuly")
    def Cash_dep(s):
        pname=input("Enter Name: ")
        ppin=int(input("Enter Pin: " ))
        if pname==s.name and ppin==s.pin:
            s.balance+=int(input("Enter the Cash Amount: "))
        else:
            print("Invalid Pin")
    def Cash_with(s):
        pname=input("Enter Name: ")
        ppin=int(input("Enter Pin: " ))
        if pname==s.name and ppin==s.pin:
            amount=int(input("Enter the Cash Amount: "))
            if amount<=s.balance:
                 s.balance-=amount
            else:
                print("Insufficient Balance")
               
        else:
            print("Invalid Pin")
    def Balance(s):
        pname=input("Enter Name: ")
        ppin=int(input("Enter Pin: " ))
        if pname==s.name and ppin==s.pin:
            print("Your remaining amount is ",s.balance)
        
            

                  


a=BankSys()
a.show_func()
a.Create_acc()
a.Cash_dep()
a.Cash_with()
a.Balance()

       
