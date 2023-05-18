class cFraction:
    def __init__(s,Numerator,Denominator):
        s.__numerator=Numerator #double underscore is used to private the object
        s.__denominator=Denominator
    def __str__(self): #str method in our class that controls how the object gets printed.
        return str(self.__numerator)+"/"+str(self.__denominator)
    def __add__(self,sf):
        a=self.__numerator
        b=self.__denominator
        c=sf.__numerator
        d=sf.__denominator
        n=a*d+b*c
        d=b*d
        o=cFraction(n,d)
        return (o)
    def FractionalValue(self):
        return self.__numerator/self.__denominator
    def __sub__(self,sf):
        a=self.__numerator
        b=self.__denominator
        c=sf.__numerator
        d=sf.__denominator
        n=a*d-b*c
        d=b*d
        o=cFraction(n,d)
        return (o)
    def __mul__(self,sf):
        if type(sf) is cFraction:
            a=self.__numerator
            b=self.__denominator
            c=sf.__numerator
            d=sf.__denominator
            n=a*c
            d=b*d
            o=cFraction(n,d)
            return (o)
        elif type(sf) is int or type(sf) is float:
            n=self.__numerator*sf
            d=self.__denominator
            o=cFraction(n,d)
            return (o)
    def __truediv__(self,sf):
        if type(sf) is cFraction:
            a=self.__numerator
            b=self.__denominator
            c=sf.__numerator
            d=sf.__denominator
            n=a*d
            d=b*c
            o=cFraction(n,d)
            return (o)
        elif type(sf) is int or type(sf) is float:
            n=self.__numerator/sf
            d=self.__denominator
            o=cFraction(n,d)
            return (o)
        
        

f1=cFraction(3,2)
f2=cFraction(5,4)
f3=f1+f2
f4=f1-f2
f5=f2*f1
f6=f1/2
print("\n","Sum of Frations: ",f3,"\n","Subtract of Fractions: ",f4,"\n","Multiply of Fractions: ",f5,"\n","Division of Fractions: ",f6)
print("\n","Sum of Frations in dec: ",f3.FractionalValue(),"\n","Subtract of Fractions in dec: ",f4.FractionalValue(),"\n","Multiply of Fractions in dec: ",f5.FractionalValue(),"\n","Division of Fractions in dec: ",f6.FractionalValue())

     


