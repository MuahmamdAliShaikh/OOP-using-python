#Python program to show how to use else clause with try and except clauses
def reciprocal(num1):
    try:
        reci=1/num1
    except ZeroDivisionError:
        print("We cannot divide by zero")
    else:
        print(reci)
reciprocal(4)
reciprocal(0)

#Python code to show the use of finally clause

#Raising an exception in try block
##try:
##    div=4//0
### this block will handle the exception raised
##except ZeroDivisionError:
##    print("Atepting to divide the zero")
### this will always be executed no matter exception is raised or not
##finally:
##    print("This is code of finally clause")

##import math
##try:
##    math.sqrt(-100)
##except ValueError as e:
##    print(e)
##

# Program to depict Raising Exception

try:
    raise NameError("try mein exception raise horahi ha") # Raise Error
except NameError:
    print ("An exception")
    raise # To determine whether the exception was raised or not

