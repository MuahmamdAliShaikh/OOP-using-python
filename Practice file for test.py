'''n=int(input("Ente the number:  "))
a=int(input("Enter the number:  "))
s=n+a
ask="Y"
while(ask=="Y"):
    ask=input("Do you want to add another number?\nEnter Y to continue: ")
    if ask=="Y":
        n=int(input("Enter the number:  "))
        s+=n
print(s)

n=int(input("Enter the number between 10 and 20: "))
while n<10 or n>20:
    if n<=10:
        print("Too low,/ntry again")
        n=int(input("Enter the number between 10 and 20"))
    elif n>=20:
        print("Too high,/try again")
        n=int(input("Enter the number between 10 and 20"))
if n>=10 or n<=20:
    print("Thank You")
l=[100,200,300]
for i in l:
    print(i)
n=int(input("Enter the three digit number "))
if n in l:
    print(l.index(n))
else:
    print("That is not in the list")
l=[]
for i in range(2):
    a=input("Enter the name:  ")
    l.append(a)
answer=input("Do you want add another name?")
while answer=="Yes" or answer=="yes":
    if answer=="Yes" or answer=="yes":
        a=input("Enter the name:  ")
        l.append(a)
        answer=input("Do you want add another name?")
print(len(l))
l=[]
for i in range(3):
    a=int(input("Enter a number: "))
    l.append(a)
user=input("Do you want to remove last number?")
if user=="Yes" or user=="yes":
    l.remove(a)
print(l)
a=[1,2,3,4,5]
b=[6,7,8,9,10]
e=[]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]%2==0:
            if b[j]%2!=0:
                e.append(a[i])
                a[i]=b[j]
                for k in range(len(e)):
                    b[j]=e[k]
print(a,b)
import random
def fun1():
    n=int(input("Enter a low number: "))
    c=int(input("Enter a high number: "))
    comp_num=random.choice(range(n,c))
    return comp_num
def fun2():
    print("I am thiking of a number: ")
    user=int(input("Guess the number  "))
    return user
def fun():
    comp_num=fun1()
    user=fun2()
    while user!=comp_num:
        if user>comp_num:
            print("Too high","\nTry again")
            user=int(input("Guess the number  "))
        elif user<comp_num:
            print("Too low","\nTry again")
            user=int(input("Guess the number  "))
    if user==comp_num:
        print("Correct You win")
    return user
fun()
import random
print("\t1.Addition")
print("\t2.Subtraction")
a=int(input('Enter the 1 0r 2: '))
if a==1:
    def addtion():
        i=random.choice(range(5,20))
        j=random.choice(range(5,20))
        user=input("Do you want to add the random numbers:  ")
        if user=="Yes" or user=="yes":
                   c=i+j
        else:
            quit()
        guess=int(input("Guess the number"))
        return c,guess
    actual,guess=addtion()
elif a==2:
    def subtraction():
        i=random.choice(range(25,50))
        j=random.choice(range(1,25))
        user=input("Do you want to add the random numbers:  ")
        if user=="Yes" or user=="yes":
                   c=i-j
        else:
            quit()
        guess=int(input("Guess the number"))
        return c,guess
    actual1,guess1=subtraction()
def fun():
    if a==1:
        if actual==guess:
            print("Correct",guess)
        else:
            print("Incorrect",actual)
    elif a==2:
        if actual1==guess1:
            print("Correct",guess1)
        else:
            print("Incorrect",actual1)
    else:
        print("Invalid number")
fun()
while True:
    l=["Ali","Mohsin","Zain"]
    opr=int(input("Enter the number of operation: "))
    if opr==1:
        a=input("Enter the name")
        l.append(a)
        print(l)
    elif opr==2:
        print(l)
        a=input("Enter the old name")
        b=input("Enter the new name")
        c=l.index(a)
        l[c]=b
        print(l)
    elif opr==3:
        print(l)
        a=input("Enter the name")
        l.remove(a)
        print(l)
    elif opr==4:
        for i in l:
            print(i)
    else:
        print("Invalid input")
file=open("Names3.txt","w")
file.write("Ali\nMohsin\nZain\n")
c=input("name")
file.write(str(c))
file=open("Names3.txt","r")
f=file.readlines()
for i in f:
    print(i)
file.close()
file=open("Names4.txt","w")
f=open("Names3.txt","r")
content=f.read()
c=input("name")
d=content.replace(c,"")
print(d)
file.write(d)
file.close()'''
print("\t1.Create a new file")
print("\t2.Display the file")
print("\t3.Add a new item to the file")
opr=int(input("Make a selecton 1,2 or 3: "))
if opr==1:
    file=open("Subject.txt","w")
    user=input("Enter the School Subject")
    file.write(user)
    #file.close()
    file.write(" ")
    file.close()
elif opr==2:
    f=open("Subject.txt","r")
    content=f.read()
    print(content)
elif opr==3:
    
    file=open("Subject.txt","a")
    a=input("Enter the new Subject")
    file.write(a)
    file.close()
    file=open("Subject.txt","r")
    content=file.read()
    print(content)
else:
    print("Invalid Input")
'''for i in range(1,5):
    for j in range(i*1):
        print(i,end=" ")
    print()'''
